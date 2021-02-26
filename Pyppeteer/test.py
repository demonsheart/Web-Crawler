import asyncio
from pyppeteer import launch


async def getRe(response):
    print('yyds')
    if response.url() == "https://enjinx.cn/eth/load/page":
        js = response.json()
        print(js)


async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto(
        'https://enjinx.cn/eth/token/0xf629cbd94d3791c9250152bd8dfbdf380e2a3b9c'
    )
    page.on('response',
            lambda response: asyncio.ensure_future(getRe(response)))
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())