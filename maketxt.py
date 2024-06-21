import os

# 이미지 파일들이 있는 디렉토리 경로
image_directory = './result/images'  # 여기에 이미지 파일들이 있는 경로를 입력하세요

# 결과를 저장할 텍스트 파일 경로
output_file_path = 'labels.txt'

# 이미지 파일 목록 가져오기
image_files = [f for f in os.listdir(image_directory) if f.endswith('.png')]

# 텍스트 파일에 기록하기
with open(output_file_path, 'w') as output_file:
    for image_file in image_files:
        file_name = os.path.splitext(image_file)[0]  # 파일 이름에서 확장자 제거
        output_file.write(f"{image_file} {file_name}\n")

print(f"이미지 파일 목록이 {output_file_path}에 기록되었습니다.")
