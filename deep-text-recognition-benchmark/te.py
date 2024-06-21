import torch

# 현재 GPU 메모리 사용량 출력
print(f"Allocated: {torch.cuda.memory_allocated() / 1024 ** 3:.2f} GB")
print(f"Cached: {torch.cuda.memory_reserved() / 1024 ** 3:.2f} GB")
print(f"Allocated: {torch.cuda.max_memory_allocated() / 1024 ** 3:.2f} GB")
print(f"Cached: {torch.cuda.max_memory_reserved() / 1024 ** 3:.2f} GB")

# GPU 캐시 메모리 정리
torch.cuda.empty_cache()

# GPU 가비지 컬렉션
import gc
gc.collect()