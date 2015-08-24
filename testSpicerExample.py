import TestSpicerAPI

testApi = TestSpicerAPI.TestSpicerAPI()

sessionId = testApi.startTest('Project', 'Suite', 'Name', 'Description', 'Functional Area', 'Risk Coverage')

age = testApi.getRandomAge(sessionId,1,13)['year']
areacode = testApi.getRandomTelephone(sessionId)['areacode']
number = testApi.getRandomTelephone(sessionId)['number']
completePhone = areacode+' '+number
email = testApi.getRandomEmail(sessionId)['email']
name = testApi.getRandomName(sessionId)['firstname']
lastname = testApi.getRandomName(sessionId)['lastname']
password = testApi.getRandomAlphaNumeric(sessionId, 10)['string']
zipcode = testApi.getRandomUSAZipCode(sessionId, 10000, 99999)['number']
#there's a bug on Test Spice this should be 0,3 to generate 1 and 2 values but is actually needed to go up by one, reported it to them
day = testApi.getRandomDate(sessionId,'01011900','01011995')['day']
month = testApi.getRandomDate(sessionId,'01011900','01011995')['month']
year = testApi.getRandomDate(sessionId,'01011900','01011995')['year']

print ' '
print 'data Obtained'
print ' '
print 'Name: ' + name
print 'Lastname: ' + lastname
print 'Email: ' + email
print 'Password: ' + password
print 'Zip Code: ' + zipcode
print 'Birthdate'
print 'day: ' + day + ' month: ' + month + ' year: ' + year
print "Random Age: "+str(age)

finishTest = testApi.finishTest(sessionId)