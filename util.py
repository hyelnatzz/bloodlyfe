


def bloodMatched(donor, recipient):
    """Matches recipient to donor (str, str) ==> bool """
    blood_match = {}   #recipient matching
    if donor == recipient or donor in blood_match[recipient]:
        return True
    return False

def getSurname(name):
    return name.split(' ')[0]


