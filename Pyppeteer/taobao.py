"""案例"""
import asyncio
from pyppeteer import launch

width, height = 500, 300  # 尺寸配置
"""如果要单独写到配置高宽，需要在window-size前面加上f哦"""


async def main():
    browser = await launch(
        headless=True,
        args=['--disable-infobars', f'--window-size={width},{height}'],
    )
    page = await browser.newPage()
    await page.goto('http://www.taobao.com')
    # await page.screenshot({'path': 'example.png'})
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())