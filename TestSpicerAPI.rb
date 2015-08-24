require 'net/http'
require 'net/https'
require 'json'

$config = {:api_key => 'get_your_api_key_by_registering_at_TestSpicer',
           :host => 'testspicer.com'}


def call_api(endpoint)
    req = Net::HTTP::Get.new '/restapi/v0.1/' + endpoint
    req["Content-Type"] = "application/json"
    req["api_key"] = $config[:api_key]
    connection = Net::HTTP.start($config[:host]) { |http| http.request(req) }

    result = connection.code

    if result == "200"
        return connection.body
    else
        return false
    end
end

def return_format_tuple(result)
    if result != false
        return JSON.load(result)
    end
    return false
end

# Starting the test
def start_test(projectName, suiteName, testName, description, functionalArea, riskCoverage)
    params = URI.encode_www_form({:projectname => projectName, :suiteName => suiteName, :testName => testName, :description => description, :functionalArea => functionalArea, :riskCoverage => riskCoverage})
    result = return_format_tuple(call_api('starttest?' + params))
    return result['sessionId']

end

# Finishing the Test
def finish_test(sessionId)
    params = 'result=pass'
    return return_format_tuple(call_api('finishtest?sessionid=' << sessionId << "&" << params))
end


# DATA TO GET


# Age
def get_random_age(sessionId, above, below)
    return return_format_tuple(call_api('age?above=#{above}&below=#{below}&sessionid=#{sessionId}'))
end

# Phone number
def get_random_phone(sessionId)
    return return_format_tuple(call_api('telephone?sessionid=#{sessionId}'))
end

# Email
def get_random_email(sessionId)
    return return_format_tuple(call_api('email?sessionid=#{sessionId}'))
end

# Get Name or Lastname
def get_random_name(sessionId)
    return return_format_tuple(call_api('name?sessionid=#{sessionId}'))
end

# Get Random Alphanumeric (ex. password)
def get_random_alphanumeric(sessionId, length)
    return return_format_tuple(call_api('string/alpha-numeric/#{length}?sessionid=#{sessionId}'))
end

# Get random numeric string
def get_random_number(sessionId, above, below)
    return return_format_tuple(call_api('number?above=#{above}&below=#{below}&sessionid=#{sessionId}'))
end

# Get random date
def get_random_date(sessionId, after, before)
    return return_format_tuple(call_api('date?after=#{after}&before=#{before}&sessionid=#{sessionId}'))
end

# Get Random Lorem Ipsum
def get_random_lorem_ipsum(sessionId, para)
    return return_format_tuple(call_api('lorem?para=#{para}'))
end

# Get Random Alphabet String
def get_random_alphabet_string(sessionId, length)
    return return_format_tuple(call_api('string/en/#{length}'))
end

# Get Random Regex String
def get_random_regex_string(sessionId, length, regexp)
    return return_format_tuple(call_api('string?length=#{length}&regexp=#{regexp}'))
end