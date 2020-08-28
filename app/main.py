from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{offset}")
def read_item(offset: int = 0):
    json_compatible_item_data = jsonable_encoder(call_api(offset))
    print(offset)
    return JSONResponse(content={
        'rows': json_compatible_item_data,  # 各ページで必要なデータをもたせる
        'lastRow': 50 # 合計のデータ量をもたせる (ハードコーディングごめんなさい)
    })


def call_api(offset: int):
    '''
    BigQuery で以下のコマンドを使用して作成したもの
WITH
  athletes AS (
  SELECT
    DISTINCT CONCAT(pitcherFirstName,' ', pitcherLastName) AS athlete,
  FROM
    `bigquery-public-data.baseball.games_post_wide`
  WHERE
    pitcherFirstName IS NOT NULL
    AND pitcherFirstName != ''
  LIMIT
    1000 )
SELECT
  athlete,
  CAST(RAND() * 100 AS INT64) AS gold,
  CAST(RAND() * 100 AS INT64) AS silver,
  CAST(RAND() * 100 AS INT64) AS bronze,
FROM
  athletes
    '''

    if offset == 0:
        return [
            {
                "athlete": "Richard Hill",
                "gold": "59",
                "silver": "19",
                "bronze": "39"
            },
            {
                "athlete": "Justin Grimm",
                "gold": "71",
                "silver": "97",
                "bronze": "34"
            },
            {
                "athlete": "Kenley Jansen",
                "gold": "24",
                "silver": "55",
                "bronze": "36"
            },
            {
                "athlete": "Jacob Arrieta",
                "gold": "19",
                "silver": "8",
                "bronze": "95"
            },
            {
                "athlete": "Joseph Blanton",
                "gold": "85",
                "silver": "3",
                "bronze": "85"
            },
            {
                "athlete": "Addison Reed",
                "gold": "91",
                "silver": "31",
                "bronze": "34"
            },
            {
                "athlete": "Jeurys Familia",
                "gold": "36",
                "silver": "96",
                "bronze": "26"
            },
            {
                "athlete": "Madison Bumgarner",
                "gold": "73",
                "silver": "17",
                "bronze": "15"
            },
            {
                "athlete": "Noah Syndergaard",
                "gold": "85",
                "silver": "65",
                "bronze": "73"
            },
            {
                "athlete": "Colbert Hamels",
                "gold": "50",
                "silver": "49",
                "bronze": "31"
            }
        ]
    elif offset == 10:
        return [
            {
                "athlete": "Alexander Claudio",
                "gold": "36",
                "silver": "78",
                "bronze": "17"
            },
            {
                "athlete": "Marco Estrada",
                "gold": "1",
                "silver": "74",
                "bronze": "48"
            },
            {
                "athlete": "Anthony Barnette",
                "gold": "92",
                "silver": "76",
                "bronze": "79"
            },
            {
                "athlete": "Kenta Maeda",
                "gold": "39",
                "silver": "38",
                "bronze": "55"
            },
            {
                "athlete": "Samuel Solis",
                "gold": "25",
                "silver": "73",
                "bronze": "27"
            },
            {
                "athlete": "Grant Dayton",
                "gold": "68",
                "silver": "52",
                "bronze": "24"
            },
            {
                "athlete": "Giovany Gonzalez",
                "gold": "66",
                "silver": "2",
                "bronze": "67"
            },
            {
                "athlete": "Thomas Stripling",
                "gold": "64",
                "silver": "63",
                "bronze": "90"
            },
            {
                "athlete": "Shawn Kelley",
                "gold": "64",
                "silver": "53",
                "bronze": "15"
            },
            {
                "athlete": "Oliver Perez",
                "gold": "10",
                "silver": "33",
                "bronze": "63"
            }
        ]
    elif offset == 20:
        return [
            {
                "athlete": "Pedro Baez",
                "gold": "88",
                "silver": "59",
                "bronze": "61"
            },
            {
                "athlete": "Joshua Fields",
                "gold": "19",
                "silver": "71",
                "bronze": "19"
            },
            {
                "athlete": "Luis Avilan",
                "gold": "8",
                "silver": "100",
                "bronze": "77"
            },
            {
                "athlete": "Mark Melancon",
                "gold": "10",
                "silver": "21",
                "bronze": "66"
            },
            {
                "athlete": "Bryan Shaw",
                "gold": "43",
                "silver": "43",
                "bronze": "19"
            },
            {
                "athlete": "Joseph Kelly",
                "gold": "59",
                "silver": "41",
                "bronze": "36"
            },
            {
                "athlete": "Matthew Barnes",
                "gold": "67",
                "silver": "47",
                "bronze": "3"
            },
            {
                "athlete": "Corey Kluber",
                "gold": "72",
                "silver": "5",
                "bronze": "89"
            },
            {
                "athlete": "Daniel Otero",
                "gold": "46",
                "silver": "55",
                "bronze": "43"
            },
            {
                "athlete": "David Price",
                "gold": "40",
                "silver": "36",
                "bronze": "79"
            }
        ]
    if offset == 30:
        return [
            {
                "athlete": "Craig Kimbrel",
                "gold": "72",
                "silver": "47",
                "bronze": "44"
            },
            {
                "athlete": "Kyle Hendricks",
                "gold": "6",
                "silver": "3",
                "bronze": "1"
            },
            {
                "athlete": "Clayton Kershaw",
                "gold": "16",
                "silver": "22",
                "bronze": "12"
            },
            {
                "athlete": "Albertin Chapman",
                "gold": "62",
                "silver": "49",
                "bronze": "33"
            },
            {
                "athlete": "Tanner Roark",
                "gold": "12",
                "silver": "29",
                "bronze": "30"
            },
            {
                "athlete": "Marc Rzepczynski",
                "gold": "22",
                "silver": "73",
                "bronze": "62"
            },
            {
                "athlete": "Blake Treinen",
                "gold": "89",
                "silver": "46",
                "bronze": "53"
            },
            {
                "athlete": "Travis Wood",
                "gold": "44",
                "silver": "81",
                "bronze": "5"
            },
            {
                "athlete": "Santiago Casilla",
                "gold": "22",
                "silver": "10",
                "bronze": "95"
            },
            {
                "athlete": "Michael Montgomery",
                "gold": "83",
                "silver": "22",
                "bronze": "90"
            }
        ]
    if offset == 40:
        return [
            {
                "athlete": "George Kontos",
                "gold": "92",
                "silver": "45",
                "bronze": "14"
            },
            {
                "athlete": "Hunter Strickland",
                "gold": "51",
                "silver": "51",
                "bronze": "11"
            },
            {
                "athlete": "Carl Edwards",
                "gold": "86",
                "silver": "62",
                "bronze": "70"
            },
            {
                "athlete": "Hector Rondon",
                "gold": "43",
                "silver": "62",
                "bronze": "51"
            },
            {
                "athlete": "Tyson Blach",
                "gold": "90",
                "silver": "40",
                "bronze": "96"
            },
            {
                "athlete": "Javier Lopez",
                "gold": "36",
                "silver": "34",
                "bronze": "44"
            },
            {
                "athlete": "Derek Law",
                "gold": "32",
                "silver": "84",
                "bronze": "23"
            },
            {
                "athlete": "James Happ",
                "gold": "5",
                "silver": "43",
                "bronze": "91"
            },
            {
                "athlete": "Joseph Biagini",
                "gold": "45",
                "silver": "79",
                "bronze": "34"
            },
            {
                "athlete": "Roberto Osuna",
                "gold": "99",
                "silver": "25",
                "bronze": "43"
            }
        ]

