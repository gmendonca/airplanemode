from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
import json


def get_number(element):
    return int(element.text.replace('.', ''))


class LowestFare:
    def __init__(self, where, to, depart, back):
        self.where = where
        self.to = to
        self.depart = depart
        self.back = back

    def find(self):
        url = "http://www.decolar.com/shop/flights/results/roundtrip/%s/%s/%s/%s/1/0/0?from=SB" % (self.where, self.to, self.depart, self.back)
        driver = webdriver.Chrome()

        lowest_prices = {}

        driver.get(url)
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME,'eva-tabs')))

            items = driver.find_element_by_class_name('cluster').find_elements_by_class_name('data')
            name = '; '.join([item.text.replace('\n', ' ').replace('\r', '') for item in items])

            price_table = driver.find_element_by_class_name('matrix-container')
            airlines = price_table.find_elements_by_class_name('matrix-airlines')
            for airline_elem in airlines:
                prices = airline_elem.find_elements_by_css_selector('.amount')
                airline = airline_elem.find_element_by_css_selector('.airline-name').text
            lowest_prices[airline] = min([get_number(price) for price in prices])

            print driver.title

            print 'name: %s' % name
            print 'lowest_price: %s available on %s' % (min(lowest_prices.values()), url)

            return json.dumps({
                'name': name,
                'lowest_price': min(lowest_prices.values()),
                'url': url
            })
        finally:
            driver.quit()

if __name__ == '__main__':
    import getopt


    def usage():
        print """\
Usage: airplanehub [OPTIONS]

Finds lowest fare.

   -f, --from                     From which airport (XXX)
   -t, --to                       To which airpot (XXX)
   -d, --depart                   Departure date (yyyy-mm-dd)
   -r, --return                   Return date (yyyy-mm-dd)
"""

    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:t:d:r:", ["from=", "to=", "depart=", "return="])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)

    where = None
    to = None
    depart = None
    back = None

    for o, a in opts:
        if o in ("-f", "--from"):
            where = a
        elif o in ("-t", "--to"):
            to = a
        elif o in ("-d", "--depart"):
            depart = a
        elif o in ("-r", "--return"):
            back = a
        else:
            assert False, "Unhandled option"

    if not where or not to or not depart or not back:
        print "Parameters not specified!"
        usage()
        sys.exit(2)

    lf = LowestFare(where, to, depart, back)
    lf.find()
