import dlib 
import numpy as np
import face_recognition_models
from sklearn.svm import SVC
import streamlit as st

from src.database.db import get_all_students

@st.cache_resource # load the model only once in system as its heavy work
def load_dlib_models():
    detector = dlib.get_frontal_face_detector()

    sp = dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )

    facerec = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )

    return detector, sp, facerec

def get_face_embeddings(image_np):
    detector, sp, facerec = load_dlib_models()
    faces = detector(image_np, 1) # 1-> manipulate image once (otherwise it try to get better results by changing image size,orientation and... and zoom image better BUT it utilizes more memory space)
    # more the no. -> more it will do image processing to recognize image better

    encodings = []

    for face in faces:
        shape = sp(image_np, face) #get landmarks of that face
        face_descriptor = facerec.compute_face_descriptor(image_np, shape, 1) #create 128 embeddings

        encodings.append(np.array(face_descriptor))

    return encodings

@st.cache_resource
def get_trained_model(): #it will get all students from DB and fir them in our Model(train the model i.e SVC model to classify the student)
    # X -> students embedding and y-> students ID to send if get matched
    X = []
    y = []

    students_db = get_all_students()

    if not students_db:
        return None

    for student in students_db:
        embedding = student.get('face_embedding')
        if embedding:
            X.append(np.array(embedding))
            y.append(student.get('student_id'))

    if len(X) == 0:
        return 0

    clf = SVC(kernel="linear",probability=True, class_weight='balanced') # linear -> separate them linearly with straight line
    # probability=True-> get prob of how much the student matches
    # class_weight='balanced' -> if one student has multiple images -> the model will get Bias toward that and will say he is present for all=> so we balance those multiple images of single student into 1 image for training
    try:
        clf.fit(X,y)
    except ValueError:
        pass

    return {'clf':clf, 'X':X, 'y':y}


def train_classifier(): #when new Student Joins
    st.cache_resource.clear() #clear cache Data to store new trained Data
    model_data = get_trained_model()
    return bool(model_data) #if something Data is outputed ->return true

def predict_attendance(class_image_np):#take attendence of students from Classroom Image
    encodings = get_face_embeddings(class_image_np) #get all embedding of all faces visible

    detected_student = {}

    model_data = get_trained_model()

    if not model_data:
        return detected_student, [], len(encodings) # (embeddings of the students ,list of all students present, no. of students)

    clf = model_data['clf']
    X_train = model_data['X']
    y_train = model_data['y']

    all_students = sorted(list(set(y_train))) #set->get unique student (if double IDs)

    for encoding in encodings:
        if len(all_students)>=2:
            predicted_id = int(clf.predict([encoding])[0]) #student highest highest score(probability)
        else: #if there is only 1 student
            predicted_id = int(all_students[0])

        student_embedding = X_train[y_train.index(predicted_id)] # index on y predicted ,that index is embedding index of that student

        # Check mathematically if they matched with actual image embeddings using linear algebra
        best_match_score = np.linalg.norm(student_embedding - encoding)  #actual image - predicted image embedding

        resemblance_threshold = 0.6 #score of each point must not be greater than 0.6 => if greater than 0.6 means the faces are very different

        if best_match_score <= resemblance_threshold:
            detected_student[predicted_id] = True

    return detected_student, all_students, len(encodings)
