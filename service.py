import model

def verify():
    return model.verify()

def sign_in(member: model.Member):
    response = model.sign_in(member)
    response.status = 200
    return response

def sign_up(member: model.Member):
    response = model.sign_up(member)
    response.status = 200
    return response

def get_lectures():
    response = model.get_lectures()
    response.status = 200
    return response

def find_lectures(lecture_id, name, category, credit):
    response = model.find_lectures(lecture_id, name, category, credit)
    response.status = 200
    return response
