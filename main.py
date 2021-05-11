import webscrapers.CDC as CDC
import webscrapers.JSI as JSI
import webscrapers.JohnsHopkins as JohnsHopkins
import webscrapers.R4D as R4D
import webscrapers.Sabin as Sabin
import webscrapers.Thinkwell as Thinkwell
import webscrapers.UNICEF as UNICEF
import webscrapers.BMFG as BMFG
import webscrapers.MSH as MSH
import webscrapers.GAVI as GAVI
from gsheets import writetosheets
from gsheets import init
import time

webscrapers = [CDC,JSI,R4D,Sabin,Thinkwell,UNICEF,BMFG,MSH,GAVI,JohnsHopkins]
def run(webscrapers):
    print("***  starting webscraping  ***")

    overall_start = time.time()

    worksheet = init()
    for webscraper in webscrapers:
        print(f"running webscraper {webscraper.name()}")
        start_time = time.time()

        try:
            df = webscraper.run()
            writetosheets(df,worksheet)
        except Exception as e:
            print(f"Error: {str(e)}")


        print(f"..finished scraping in a total of {minutes_from(start_time)} minutes")

    print(f"*** finished all webscrapers in {minutes_from(overall_start)}***")

def minutes_from(start):
    return '%.2f' % ((time.time() - start)/60)

if __name__ == "__main__":
    run(webscrapers)
