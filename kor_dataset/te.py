import io
from PIL import Image
import lmdb

# 가져올 이미지의 키
image_key = b'image-000000001'  # 예시: 첫 번째 이미지의 키
output_image_path = "./output_image.png"  # 저장할 이미지 파일 경로

# LMDB 환경 열기 (읽기 전용)
env = lmdb.open('./deep-text-recognition-benchmark/made1_data_lmdb/train', readonly=True)

# 데이터베이스 트랜잭션 시작
with env.begin() as txn:
    # 특정 키에 대한 데이터 가져오기
    image_bin = txn.get(image_key)

# 이진 데이터를 이미지로 변환하여 저장
if image_bin is not None:
    # 이진 데이터를 이미지로 디코딩
    image = Image.open(io.BytesIO(image_bin))
    # 이미지를 지정된 경로에 저장
    image.save(output_image_path)
    print("Image saved successfully to:", output_image_path)
else:
    print("Image not found in the LMDB dataset.")
