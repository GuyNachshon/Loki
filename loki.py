import click
from main import main
from main import USERNAME, REPO_TO_COMMIT, REPO_GIT_DIR

LOKI_LOGO = """
           .7!!!7.                       ^^:.               .^^^^^^^      .:   ~5?.^YGB~            
           ~GGGGG^                    .~5GGBBP?^           .JJJJJJJ^     ^:    :B&&&&B.             
           ^GPPPG^                 .!P: ^  .^JGBG!         ??????J^    ^:       ~&&&&!              
           ^GPPPG^              .: :BB. :      ~GBY   .   7J????J^   ::         ~&&&&!              
           ^GPPPG^             7Y  .GG. ^.      :PB?     7J????J~  :~.          ~&&&&!              
           ^GPPPG^            :G.  .GG. :        !BG    !J????J! .7J?7???!      ~&&&&!              
           ^GPPPG^            JG   .GB. :        ~BY   !J??????7!J?????J!       ~&&&&!              
           ^GPPPG^            5B.  .BG. :.       YP.  ~J?????7.!J???????        ~&&&&!              
           ^GPPPG:            !B5  :5:  :       !Y   ~J??????. ????????7        ~&&&&!              
           ^GPPPP7..........   YBY:.    .      ~^   ^J??????.  ?????????:    .  ~&&&&!              
           ^GPPPPPPPPPPPPPPJ    ?BB?:   .   .^:    :J?????J.   ~J????????7!!!.  G&&&&G5?            
            YGPPPPPPPPPPPGJ      .7PGG5Y5?7~:     :JJ????J:     ^7?JJJJJ??!:    :?B&&&B7            
             ^?YYYYYYYYYY?          ..::..        ........        ..:::..          ~5~              
"""


@click.command()
@click.option('--message', '-m', default='We Are Not Doing "Get Help."', help='The commit message')
@click.argument('username')
def loki(username, message):
    print(LOKI_LOGO)
    main(username, message)
    print(f"faked commit\ngo to https://github.com/{USERNAME}/{REPO_TO_COMMIT} to see the commit")
