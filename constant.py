#LCGParameters
SEED = 1013904221
MULTIPLIER = 1664525
INCREMENT = 1013904223
MODULE = 4294967296	

#OrdersCount
ORDER_CREATED_BEFORE_START = 600
ORDER_DONE_AFTER_FINISH = 200
ORDER_IN_TIME = 1200
COUNT_RECORDS = 7200
COUNT_ORDERS = 2000
MIN_COUNT_RECORDS = 3
MAX_COUNT_RECORDS = 4

#INSTRUMENTS
COUNT_INSTRUMENT = 11
INSTRUMENTS = [
    "GBPRUB",
    "EURRUB",
    "USDRUB",
    "EURUSD",
    "CNYRUB",
    "EURJPY",
    "EURCHF",
    "USDJPY",
    "GBPUSD",
    "USDCHF",
    "GBPUAH"
]

PX_INIT = [
    [103.773, 0.001],
    [91.6835, 0.0001],
    [75.723, 0.001],
    [1.21, 0.01],
    [11.81, 0.01],
    [125.13, 0.01],
    [1.076, 0.001],
    [103.87, 0.01],
    [1.37, 0.01],
    [0.889, 0.001],
    [35.571, 0.001]
]
#
DIVIDER_PX_INIT = 10000
DIVIDER_VOLUME_INIT = 1000000
DIVIDER_SIDE = 10000000
DIVIDER_STATUS = 1000000000
DIVIDER_PX_FILL = 10000000
DIVIDER = 10000
DIVIDER_PX_INIT_CHANGE = 1000
DIVIDER_TAG = 1000
#
SIDE = [
    "Buy",
    "Sell"
]

STATUS = [
    "New",
    "In process",
    ["Fill","PartialFil","Cancel"],
    "Done"
]

TAGS_COUNT = 7
TAG = [
    "tag1",
    "tag2",
    "tag3",
    "tag4",
    "tag5",
    "tag6",
    "tag7"
]

COUNT_NOTE = 11
NOTE = [
    "Note1",
    "Note2",
    "Note3",
    "Note4",
    "Note5",
    "Note6",
    "Note7",
    "Note8",
    "Note9",
    "Note10",
    "Note11"
]

YEAR = 2021
MONTH = 2
DAY = 2
DATE_FORMAT = '%Y-%m-%d %H:%M:%S.%f'
MILLISECONDS = 1000000

DATE_FORMAT_FOR_MYSQL = "INSERT INTO 'task'.'order' VALUES ('{id}','{instrument}','{px_init}','{px_fill}','{side}','{volume_init}','{volume_fill}','{status}','{date}','{note}','{tags}')"