import httplib
import urllib
try:
    import json
except ImportError:
    import simplejson as json

config = {"api_key": "get_your_api_key_by_registering_at_TestSpicer",
          "host": "testspicer.com"}

class TestSpicerAPI():

    def callAPI( self, endpoint ):
        connection = httplib.HTTPConnection(config['host'])
        connection.request('GET', '/restapi/v0.1/' + endpoint,
                           headers={"Content-Type": "application/json", "api_key": config['api_key']})

        result = connection.getresponse()
        if result.status == 200:
            return result.read()
        else:
            return False

    def returnFormatTuple(self, result ):
        if result is not False:
            return json.loads( result )
        return False

    # for starting the test
    def startTest(self, projectName, suiteName, testName, description, functionalArea, riskCoverage):
        params = urllib.urlencode({ 'projectname':projectName, 'suitename':suiteName, 'name':testName, 'description':description, 'functionalarea':functionalArea, 'riskcoverage':riskCoverage })
        result = self.returnFormatTuple( self.callAPI( 'starttest?' + params ) )
        return result['sessionId']

    # Data to get
    # Age
    def getRandomAge(self, sessionId, above, below ):
        return self.returnFormatTuple( self.callAPI('age?above=%s&below=%s&sessionid=%s' % (above,below,sessionId)))

    # Phone number
    def getRandomTelephone(self, sessionId ):
        return self.returnFormatTuple( self.callAPI('telephone?sessionid=%s' % sessionId))

    # Email
    def getRandomEmail(self, sessionId):
        return self.returnFormatTuple (self.callAPI('email?sessionid=%s' % sessionId))

    # Get Name or Lastname
    def getRandomName(self, sessionId):
        return self.returnFormatTuple (self.callAPI('name?sessionid=%s' % sessionId))

    # Get Random Alphanumeric (ex. password)
    def getRandomAlphaNumeric(self, sessionId, length):
        return self.returnFormatTuple (self.callAPI('string/alpha-numeric/%s?sessionid=%s' % (length, sessionId )))

    # Get random numeric, 5 digit string
    def getRandomUSAZipCode(self, sessionId, above, below):
        return self.returnFormatTuple(self.callAPI('number?above=%s&below=%s' % (above, below)))

    # Get random dates
    def getRandomDate(self, sessionId, after, before ):
        return self.returnFormatTuple(self.callAPI('date?after=%s&before=%s' % (after, before)))

    # Get Random Lorem Ipsum
    def getRandomLorem(self, sessionId, para ):
        return self.returnFormatTuple(self.callAPI('lorem?para=%s' % (para)))

    # Get Random Alphhabets String
    def getRandomLorem(self, sessionId, lenght ):
        return self.returnFormatTuple(self.callAPI('string/en/%s' % (lenght)))

    # Get Regex String
    def getRandomLorem(self, sessionId, lenght, regexp ):
        return self.returnFormatTuple(self.callAPI('string?length=%s&regexp=%s' % (lenght, regexp)))
   
    # use when finishing the test
    def finishTest(self,sessionId):
        params = 'result=pass'
        return self.returnFormatTuple(self.callAPI('finishtest?sessionid=%s' % sessionId + params))