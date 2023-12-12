import os
import pydicom

def set_patient_id(directory_path, new_patient_id, out_dir):
    # Iterate through all files in the directory
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith('.dcm'):
                # Form the full path to the DICOM file
                dicom_file_path = os.path.join(root, file_name)
                out_file_path = os.path.join(out_dir, file_name)

                # Load the DICOM file
                ds = pydicom.dcmread(dicom_file_path)

                # Set the PatientID attribute
                ds.PatientID = new_patient_id

                # Save the modified DICOM file
                ds.save_as(out_file_path)
                print(f"PatientID set for {out_file_path}")

# Specify the directory containing DICOM files
in_dir = '//rovelocity/import/12/12/2023_DailyQA'
out_dir = os.path.join(in_dir, 'out')
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

# Specify the new PatientID
new_patient_id = '12122023'

# Set PatientID for all DICOM files in the directory
set_patient_id(in_dir, new_patient_id, out_dir)

print('done.')