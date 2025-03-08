#include <iostream>
#include <Queue>

#define DefaultNumVertex 20

using namespace std;

template <class edgeType>
struct edgeNode
{
    int dest;
    edgeType weight;
    edgeNode *link;
};

template <class verType, class edgeType>
struct verNode
{
    verType data;
    edgeNode<edgeType> *adj;
};

template<class verType, class edgeType>
class Graph
{
private:
    int verts, edges;
    int maxVertex;
    verType *verList;
    edgeType **edgeMatrix;
    edgeType noEdge;
    bool directed;
    void DFS(int start, bool visited[])const;
public:
    Graph(bool direct, edgeType e);
    ~Graph();
    int numberOfVertex()const{return verts;};
    int numberOfEdge()const{return edges;};
    int getVertex(verType vertex)const;
    bool existEdge(verType vertex1, verType vertex2) const;
    void insertVertex(verType vertex);
    void insertEdge(verType vertex1, verType vertex2, edgeType edge);
    void removeVertex(verType vertex);
    void removeEdge(verType vertex1, verType vertex2);

    int getFirstNeighbor(verType vertex)const;
    int getNextNeighbor(verType vertex1, verType vertex2)const;
    void disp()const;
    void DFS()const;
    void BFS()const;
    bool connected()const;
};

template <class verType, class edgeType>
Graph<verType, edgeType>::Graph(bool direct, edgeType e)
{
    int i, j;
    //初始化属性
    directed = direct;
    noEdge = e;
    verts = 0;
    edges = 0;
    maxVertex = DefaultNumVertex;
    //为存顶点的一维数组和存边的二维数组创建空间
    verList = new verType[maxVertex];
    edgeMatrix = new edgeType*[maxVertex];
    //初始化图结构g，direct为是否有向图标志，e为无边数据
    for (i=0; i<maxVertex; i++)
        edgeMatrix[i] = new edgeType[maxVertex];

    //初始化二维数组，边的个数为0
    for (i=0; i<maxVertex; i++)
        for (j=0; j<maxVertex; j++)
            if (i==j)
                edgeMatrix[i][j] = 0;//对角线元素
            else
                edgeMatrix[i][j] = noEdge; //无边
}

template <class verType, class edgeType>
Graph<verType, edgeType>::~Graph()
{
    int i;
    delete []verList;
    for (i=0; i<maxVertex; i++)
        delete []edgeMatrix[i];
    delete []edgeMatrix;
}

//返回顶点为vertex值的元素在顶点表中的下标
template <class verType, class edgeType>
int Graph<verType, edgeType>::getVertex(verType vertex) const
{
    int i;
    for (i=0; i<verts; i++)
        if (verList[i]==vertex)
            return i;
    return -1;
}

//判断某两个顶点是否有边
template <class verType, class edgeType>
bool Graph<verType, edgeType>::existEdge(verType vertex1,verType vertex2)const
{
    int i, j;
    //找到vertex1和vertex2的下标
    for (i=0; i<verts; i++)
        if (verList[i]==vertex1)
            break;
    for (j=0; j<verts; j++)
        if (verList[j]==vertex2)
            break;
    if (i==verts || j==verts)
        return false;
    if(i==j)
        return false;
    if (edgeMatrix[i][j] == noEdge)
        return false;
    return true;
}

//删除顶点
template <class verType, class edgeType>
void Graph<verType, edgeType>::removeVertex(verType vertex)
 //删除顶点
{
    int i, j, k;
    //找到该顶点在顶点表中的下标
    for (i=0; i<verts; i++)
        if (verList[i]==vertex)
            break;
    if (i==verts)
        return;
    //在顶点表中删除顶点
    for (j=i; j<verts-1; j++)
        verList[j] = verList[j+1];

    //计数删除顶点射出的边,边数减少
    for (j=0; j<verts; j++)
        if ((j!=i) && (edgeMatrix[i][j]!= noEdge))
            edges--;
    //如果是有向图，计数删除顶点射入的边,边数减少
    if (directed)
    {
        for (k=0; k<verts; k++)
        if (((k!=i) && edgeMatrix[k][i]!= noEdge))
            edges--;
    }
    //第i行之后所有行上移
    for (j=i; j<verts-1; j++)
    {
        for (k=0; k<verts; k++)
        {
            edgeMatrix[j][k] = edgeMatrix[j+1][k];
        }
    }
    //第i列之后所有列前移
    for (j=i; j<verts-1; j++)
    {
        for (k=0; k<verts; k++)
        edgeMatrix[k][j] = edgeMatrix[k][j+1];
    }
    verts--;
}

template <class verType, class edgeType>
void Graph<verType, edgeType>::DFS() const
{
    bool *visited;
    int i;
    visited = new bool[verts];
    for (i=0; i<verts; i++)
        visited[i]=false;
    for (i=0; i<verts; i++)
    {
        if (!visited[i])
            DFS(i, visited);
        cout<<endl;
    }
}

template <class verType, class edgeType>
void Graph<verType, edgeType>::DFS(int start, bool visited[])const
{
    edgeNode<edgeType> *p;
    cout<<verList[start].data<<'\t';     visited[start] = true;    p = verList[start].adj;
    while (p)
    {
        if (!visited[p->dest])
            DFS(p->dest, visited);
        p = p->link;
    }
}

template <class verType, class edgeType>
void Graph<verType, edgeType>::BFS()const//广度优先遍历
{
    queue<int> q;
    edgeNode<edgeType> *p;
    bool *visited;
    int i, start;
    //为visited创建动态数组空间，并置初始访问标志为false。
    visited = new bool[verts];
    for (i=0; i<verts; i++)
        visited[i]=false;
    //逐一找到未被访问过顶点，
    //做广度优先遍历
    for (i=0; i<verts; i++)
    {
        if (visited[i])
            continue;
        q.push(i);
        while (!q.empty())
        {
            start = q.front();
            q.pop();
            if (visited[start])
                continue;
            cout << verList[start].data<<'\t';
            visited[start] = true;
            p = verList[start].adj;
	        while (p)
	        {
	            if (!visited[p->dest])
                    q.push(p->dest);
                p = p->link;
	        }
	    }
	    cout<<'\n';
	}
}

template <class verType, class edgeType>
bool Graph<verType, edgeType>::connected()const//广度优先遍历
{
    queue<int> q;
    edgeNode<edgeType> *p;
    bool *visited;
    int i, start, count_=0;
    //count为计数器
    //为visited创建动态数组空间，并置初始访问标志为false。
    visited = new bool[verts];
    for (i=0; i<verts; i++)
        visited[i]=false;
     //逐一找到未被访问过顶点，
  //做广度优先遍历
    for (i=0; i<verts; i++)
    {
        if (visited[i])
            continue;
        q.push(i);
        count_++;
        while (!q.empty())
        {
            start = q.front();
            q.pop();
            if(visited[start])
                continue;
            cout<<verList[start].data<<'\t';
            visited[start] = true;
            p = verList[start].adj;
	        while (p)
            {
                if (!visited[p->dest])
                    q.push(p->dest);
                    p = p->link;
            }
        }
        cout<<'\n';
    }
    if (count_==1)
        return true;
    return false;
}


int main()
{
    cout << "Hello world!" << endl;
    return 0;
}
