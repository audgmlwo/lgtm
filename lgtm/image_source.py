from io import BytesIO
import requests
from pathlib import Path

class LocalImage:
    """파일에서 이미지를 가져오는 클래스"""

    def __init__(self, path):
        self._path = path

    def get_image(self):
        # 파일을 읽기 모드로 열어서 반환
        return open(self._path, 'rb')


class RemoteImage:
    """URL에서 이미지를 가져오는 클래스"""

    def __init__(self, path):
        self._url = path

    def get_image(self):
        # URL에서 데이터를 요청
        data = requests.get(self._url)
        # 바이트 데이터를 파일 객체로 변환하여 반환
        return BytesIO(data.content)


class _LoremFlickr(RemoteImage):
    """키워드 검색으로 이미지를 가져오는 클래스"""
    LOREM_FLICKR_URL = 'https://loremflickr.com'
    WIDTH = 800
    HEIGHT = 600

    def __init__(self, keyword):
        # 부모 클래스의 생성자를 호출하여 URL을 생성
        super().__init__(self._build_url(keyword))

    def _build_url(self, keyword):
        # 키워드에 맞는 URL을 생성하여 반환
        return (f'{self.LOREM_FLICKR_URL}/'
                f'{self.WIDTH}/{self.HEIGHT}/{keyword}')


KeywordImage = _LoremFlickr

# 함수지만 생성자로 사용
def ImageSource(keyword):
    """최적의 이미지 소스 클래스를 반환하는 함수"""
    if keyword.startswith(('http://', 'https://')):
        # URL이 주어진 경우 RemoteImage 인스턴스 반환
        return RemoteImage(keyword)
    elif Path(keyword).exists():
        # 경로가 존재하는 경우 LocalImage 인스턴스 반환
        return LocalImage(keyword)
    else:
        # 키워드로 이미지를 가져올 경우 KeywordImage 인스턴스 반환
        return KeywordImage(keyword)


def get_image(keyword):
    """이미지 파일 객체를 반환하는 함수"""
    return ImageSource(keyword).get_image()