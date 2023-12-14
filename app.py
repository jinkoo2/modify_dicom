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

def set_patient_id_name(directory_path, new_patient_id, new_patient_name, out_dir):
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
                ds.PatientName = new_patient_name

                # Save the modified DICOM file
                ds.save_as(out_file_path)
                #print(f"PatientID set for {out_file_path}")

def sub_dirs(directory):
    return [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]

import zipfile

def zip_all_files_in_folder(folder_path, zip_file_name):
    with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(folder_path, '..')))

# # Specify the directory containing DICOM files
# in_dir = '//rovelocity/import/12/12/2023_DailyQA'
# out_dir = os.path.join(in_dir, 'out')
# if not os.path.exists(out_dir):
#     os.mkdir(out_dir)

# # Specify the new PatientID
# new_patient_id = '12122023'

# # Set PatientID for all DICOM files in the directory
# set_patient_id(in_dir, new_patient_id, out_dir)

root_dir = '//uhmc-fs-share/shares/Clinical_Trials/RadOnc/POTEN-C/cases'
IID = '08-SBUH'
for case_dir_name in sub_dirs(root_dir):
    print(case_dir_name)
    caseID = case_dir_name.split('_')[0]
    new_patient_id = f'POTEN-C0{caseID}'
    new_patient_name = f'{new_patient_id}^{IID}'
    case_dir = os.path.join(root_dir, case_dir_name)
    print('caseID=', caseID)
    print('new_patient_id=', new_patient_id)
    print('new_patient_name=', new_patient_name)

    for study_dir_name in sub_dirs(case_dir):
        study_dir = os.path.join(case_dir, study_dir_name)
        print('study_dir_name=', study_dir_name)

        dir = study_dir
        out_dir = os.path.join(dir, 'anonymized')
        if not os.path.exists(out_dir):
            os.mkdir(out_dir)

        #set_patient_id_name(dir, new_patient_id, new_patient_name, out_dir)

        zip_file_name = f'{IID}_POTEN-C0{caseID}.{study_dir_name}.zip'
        zip_file = os.path.join(study_dir, zip_file_name)
        if not os.path.exists(zip_file):
            print('zipping... to '+zip_file)
            zip_all_files_in_folder(out_dir, zip_file)


# dir = '//uhmc-fs-share/shares/Clinical_Trials/RadOnc/POTEN-C/cases/801_Michael_Taber_00699391/mr_dicom'
# out_dir = os.path.join(dir, 'anonymized')
# if not os.path.exists(out_dir):
#     os.mkdir(out_dir)


# IID = '08'
# new_patient_id = 'POTEN-C0801'
# new_patient_name = f'{new_patient_id}^{IID}-SBUH'
# set_patient_id_name(dir, new_patient_id, new_patient_name, out_dir)

print('done.')