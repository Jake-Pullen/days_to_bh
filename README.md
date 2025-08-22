# 🎉 UK Bank Holiday Countdown 🎉

### Because everyone needs to know when they can finally take a break from work

## What is this?

This nifty Python script fetches the latest UK bank holidays from the official GOV.UK API and tells you exactly how many days until the next one. Because apparently, we all need to be reminded that we're not working on Mondays.

---

## Features
 
✅ Fetches real-time bank holiday data from GOV.UK
✅ Calculates days until next holiday (because counting is hard)
✅ Handles edge cases like today being a bank holiday 🎉
✅ Shows special messages for tomorrow's holidays
✅ No dependencies beyond standard library (except if you want dateutil)

### Installation

`uv sync`


### Usage

`uv run main.py`

### Example Output

```Fetching UK Bank Holidays...

Next Bank Holiday:
Title: New Year's Day
Date: 01/01/2024
Days until: 5

Next Bank Holiday:
Title: Good Friday
Date: 07/04/2024
Days until: 0
Today is a bank holiday! 🎉
```
### Why?

Because we all have that one colleague who keeps asking "How many days till the next bank holiday?" and we're too polite to tell them to check their phone.

### Disclaimer

This script does not guarantee:

That you'll actually take your holiday
That the government won't change their mind about holidays
That your boss will let you go on holiday
But it does guarantee that you'll know exactly when the next one is!

Made with ❤️ and ☕ by someone who's definitely going to take their holiday
