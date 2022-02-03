


def bloodMatched(recipient, donor):
    """Matches recipient to donor (str, str) ==> bool """
    blood_match = {"A-": ["A-", "O-", "AB-"], 
                   "A+":["A+","A-", "O-", "O+"],
                   "B-":["B-", "O-"],
                   "B+":["B+", "B-", "O+", "O-"],
                   "O-":["O-"],
                   "O+":["O-", "O+"],
                   "AB+":["A+","A-", "B+", "B-", "AB-", "AB+", "O-", "O+"],
                   "AB-":["O-", "B-", "A-", "AB-"]}   #recipient matching
    return donor == recipient or donor in blood_match[recipient]





