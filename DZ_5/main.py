import platform
import aiohttp
import asyncio
import sys
from datetime import datetime, timedelta

async def fetch_exchange_rate_for_date(session, date):
    formatted_date = date.strftime('%d.%m.%Y')
    url = f"https://api.privatbank.ua/p24api/exchange_rates?json&date={formatted_date}"
    try:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                result = {}
                for rate in data['exchangeRate']:
                    if rate['currency'] in ('USD', 'EUR'):
                        if 'saleRate' in rate and 'purchaseRate' in rate:
                            if formatted_date not in result:
                                result[formatted_date] = {}
                            result[formatted_date][rate['currency']] = {
                                'sale': rate['saleRate'],
                                'purchase': rate['purchaseRate']
                            }
                return result
            else:
                print(f"Request error: HTTP status {response.status} for date {formatted_date}")
                return None
    except aiohttp.ClientError as e:
        print(f"Network error when requesting exchange rate for date {formatted_date}: {e}")
        return None

async def fetch_exchange_rates_for_period(days):
    results = []
    async with aiohttp.ClientSession() as session:
        for day in range(days):
            date = datetime.now() - timedelta(days=day)
            rate = await fetch_exchange_rate_for_date(session, date)
            if rate:
                results.append(rate)
    return results

async def main(days):
    rates = await fetch_exchange_rates_for_period(days)
    print(rates)

if __name__ == "__main__":
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    days = 1
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        days = min(int(sys.argv[1]), 10)

    asyncio.run(main(days))