import click

from lgtm.drawer import save_with_message
from lgtm.image_source import get_image

@click.command()
@click.option('--message', '-m', default='LGTM',
              show_default=True, help='이미지에 추가할 문자열')
@click.argument('keyword')
def cli(keyword, message):
    """LGTM 이미지 생성 도구"""
    lgtm(keyword, message)
    click.echo('lgtm')  # 동작 확인용


def lgtm(keyword, message):
    with get_image(keyword) as fp:
        save_with_message(fp, message)