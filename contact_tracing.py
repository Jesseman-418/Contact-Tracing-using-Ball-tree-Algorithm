# Install necessary packages
# You may need to install additional packages based on your environment and data format
# pip install pandas scikit-learn matplotlib numpy


import pandas as pd
import numpy as np
from sklearn.neighbors import BallTree
import matplotlib.pyplot as plt

# Function to calculate distances using BallTree
def calculate_distances(infected_coordinates, students_data):
    # Build BallTree using the infected person's path
    tree = BallTree(infected_coordinates)

    # Extract coordinates from student data
    student_coordinates = students_data[['X', 'Y']].values

    # Query the tree to find distances to the nearest point in the infected person's path
    distances, _ = tree.query(student_coordinates)

    return distances

# Function for contact tracing
def contact_tracing(infected_person_path, students_data, threshold_distance):
    # Convert 'Timestamp' column to datetime
    infected_person_path['Timestamp'] = pd.to_datetime(infected_person_path['Timestamp'])
    students_data['Timestamp'] = pd.to_datetime(students_data['Timestamp'])

    # Extract coordinates from the infected person's path
    infected_coordinates = infected_person_path[['X', 'Y']].values

    # Calculate distances using the calculate_distances function
    distances = calculate_distances(infected_coordinates, students_data)

    # Identify potentially infected students based on the threshold distance
    infected_students = students_data[distances < threshold_distance]

    return infected_students


def preprocess_data(data):
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    return data

def visualize_results(infected_person_path, students_data, infected_students):
    plt.scatter(students_data['X'], students_data['Y'], label='Students')
    plt.plot(infected_person_path['X'], infected_person_path['Y'], marker='o', color='red', label='infected Person')
    plt.scatter(infected_students['X'], infected_students['Y'], color='orange', label='Potentially Infected')

    plt.title('Contact Tracing Visualization')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()


infected_person_path_data = {
    'Timestamp': pd.to_datetime('today') + pd.to_timedelta(np.arange(3) * 15, unit='T'),
    'X': np.random.uniform(0, 10, 3),
    'Y': np.random.uniform(0, 10, 3),
}

students_data = {
    'StudentID': range(101, 351),  # Changed from 101 to 351
    'Name': [f'Stu_{i}' for i in range(1, 251)],  # Changed from 1 to 251
    'Timestamp': [pd.to_datetime('today')]*250,  # Changed the date to today's date and reduced the number of students to 250
    'X': np.random.uniform(0, 10, 250),  # Adjusted for 250 students
    'Y': np.random.uniform(0, 10, 250),  # Adjusted for 250 students
}


# Set the distance threshold
THRESHOLD_DISTANCE = 3
# Data preprocessing
infected_person_path = preprocess_data(pd.DataFrame(infected_person_path_data))
students_data = preprocess_data(pd.DataFrame(students_data))

def visualize_results_with_background(infected_person_path, students_data, infected_students, background_image_path):
    # Load the background image
    background_image = plt.imread("/Users/jesseman/Documents/Contact Tracing/VITimage.jpg")

    # Plot the background image
    plt.imshow(background_image, extent=[0, 10, 0, 10])

    # Scatter plot for uninfected students
    plt.scatter(students_data['X'], students_data['Y'], label='Uninfected', color='blue')

    # Plot infected person's path
    plt.plot(infected_person_path['X'], infected_person_path['Y'], marker='o', color='red', label='Infected Person')

    # Scatter plot for potentially infected students
    plt.scatter(infected_students['X'], infected_students['Y'], color='orange', label='Potentially Infected')

    # Annotate points with shortened student names
    for index, student in infected_students.iterrows():
        plt.annotate(student['Name'], (student['X'], student['Y']), textcoords="offset points", xytext=(0, 5), ha='center')

    plt.title('Contact Tracing Visualization with Background Image')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()

# Specify the path to your background image
background_image_path = '/Users/jesseman/Documents/Contact Tracing/VITimage.jpg'  # Replace with the actual path to your image


infected_students = contact_tracing(infected_person_path, students_data, THRESHOLD_DISTANCE)

# Add a column indicating infection status
students_data['InfectionStatus'] = 'Non-Infected'
students_data.loc[students_data['StudentID'].isin(infected_students['StudentID']), 'InfectionStatus'] = 'Potentially Infected'

# Save the result to a CSV file
output_filename = 'contact_tracing_results.csv'
students_data.to_csv(output_filename, index=False)

# Display a sample of the resulting DataFrame
print(students_data.head())

# Visualization with background image
visualize_results_with_background(infected_person_path, students_data, infected_students, background_image_path)
