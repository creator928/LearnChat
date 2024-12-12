import resolve_path
from chatbot.retrieval import Retrieval

retrieval = Retrieval()

# Test 1
retrieved = retrieval.retrieve("minji")

print("Test 1: below should retrieve sentence about minji")
print(retrieved)
print("===")

# Test 2
retrieved = retrieval.retrieve("not_known")

print("Test 2: below should print None")
print(retrieved)
print("===")

# Test 3
retrieved = retrieval.retrieve("haerin")

print("Test 3: case haerin")
print(retrieved)
print("===")

# Test 4
retrieved = retrieval.retrieve("hanni")

print("Test 4: case hanni")
print(retrieved)
print("===")

# Test 4
retrieved = retrieval.retrieve("null people")

print("Test 3: case null people")
print(retrieved)
print("===")
