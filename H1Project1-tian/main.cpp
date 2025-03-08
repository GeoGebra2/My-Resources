#include <iostream>
#include <vector>
#include <algorithm>

class MemoryBlock {
public:
    int start;
    int size;
    MemoryBlock* next;

    MemoryBlock(int s, int sz) : start(s), size(sz), next(nullptr) {}
};

class FreeList {
private:
    MemoryBlock* head;
    void mergeAdjacentBlocks(MemoryBlock*& block);

public:
    FreeList() : head(nullptr) {}

    void addBlocks(int n, const std::vector<int>& starts, const std::vector<int>& sizes);
    bool allocate(int request_size);
    void release(int start, int size);
    void printList() const;

    ~FreeList();
};

void FreeList::addBlocks(int n, const std::vector<int>& starts, const std::vector<int>& sizes) {
    if (n <= 0) return;

    std::vector<MemoryBlock*> blocks(n);
    for (int i = 0; i < n; ++i) {
        blocks[i] = new MemoryBlock(starts[i], sizes[i]);
    }

    std::sort(blocks.begin(), blocks.end(), [](MemoryBlock* a, MemoryBlock* b) { return a->start < b->start; });

    for (MemoryBlock* block : blocks) {
        block->next = head;
        head = block;
    }
}

bool FreeList::allocate(int request_size) {
    MemoryBlock* current = head;
    MemoryBlock* prev = nullptr;

    while (current != nullptr) {
        if (current->size >= request_size) {
            if (current->size > request_size) {
                MemoryBlock* newBlock = new MemoryBlock(current->start + request_size, current->size - request_size);
                newBlock->next = current->next;
                current->size = request_size;
                current->next = newBlock;
            }
            if (prev) {
                prev->next = current->next;
            } else {
                head = current->next;
            }
            delete current;
            return true;
        }
        prev = current;
        current = current->next;
    }
    return false;
}

void FreeList::release(int start, int size) {
    // Find the right position to insert the block
    MemoryBlock* prev = nullptr;
    MemoryBlock* current = head;
    while (current && current->start < start) {
        prev = current;
        current = current->next;
    }

    // Insert the block
    MemoryBlock* newBlock = new MemoryBlock(start, size);
    newBlock->next = current;
    if (prev) {
        prev->next = newBlock;
    } else {
        head = newBlock;
    }

    // Merge with adjacent blocks
    mergeAdjacentBlocks(newBlock);
    mergeAdjacentBlocks(newBlock->next);
}

void FreeList::mergeAdjacentBlocks(MemoryBlock*& block) {
    if (!block || !block->next) return;

    if (block->next->start == block->start + block->size) {
        block->size += block->next->size;
        block->next = block->next->next;
    }
}

void FreeList::printList() const {
    MemoryBlock* current = head;
    while (current) {
        std::cout << "(" << current->start << "," << current->size << ") ";
        current = current->next;
    }
    std::cout << std::endl;
}

FreeList::~FreeList() {
    while (head) {
        MemoryBlock* temp = head;
        head = head->next;
        delete temp;
    }
}

int main() {
    // Example usage
    int n, m;
    std::cin >> n;
    std::vector<int> starts(n), sizes(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> starts[i];
    }
    for (int i = 0; i < n; ++i) {
        std::cin >> sizes[i];
    }
    std::cin >> m;

    FreeList fl;
    fl.addBlocks(n, starts, sizes);

    for (int i = 0; i < m; ++i) {
        int op;
        std::cin >> op;
        if (op == 1) {
            int request_size;
            std::cin >> request_size;
            fl.allocate(request_size);
        } else if (op == 2) {
            int start, size;
            std::cin >> start >> size;
            fl.release(start, size);
        }
    }

    fl.printList();
    return 0;
}
