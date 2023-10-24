import os
import shutil
import random
import csv


def create_annotation_file(dataset_dir, project_dir):
    with open('annotations.csv', 'w', newline='') as annotation_file:
        writer = csv.writer(annotation_file)

        for root, dirs, files in os.walk(dataset_dir):
            for filename in files:
                class_name = os.path.basename(root)
                absolute_path = os.path.join(root, filename)
                relative_path = os.path.relpath(absolute_path, project_dir)

                writer.writerow([absolute_path, relative_path, class_name])


def copy_dataset_with_new_names(dataset_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    with open('annotations.csv', 'w', newline='') as annotation_file:
        writer = csv.writer(annotation_file)

        for root, dirs, files in os.walk(dataset_dir):
            for filename in files:
                class_name = os.path.basename(root)
                old_filepath = os.path.join(root, filename)
                new_filename = f'{class_name}_{filename}'
                new_filepath = os.path.join(output_dir, new_filename)

                writer.writerow([new_filepath, new_filename, class_name])
                shutil.copy(old_filepath, new_filepath)


def create_dataset_with_random_names(dataset_dir, output_dir):
    random_names_dir = output_dir+"\\random_names"
    os.makedirs(random_names_dir, exist_ok=True)

    random_names = [str(random.randint(0, 10000)) for _ in range(10000)]

    for root, dirs, files in os.walk(dataset_dir):
        for filename in files:
            class_name = os.path.basename(root)
            old_filepath = os.path.join(root, filename)
            random_name = random_names.pop()
            new_filename = f'{random_name}.jpg'
            new_filepath = os.path.join(random_names_dir, new_filename)
            shutil.copy(old_filepath, new_filepath)


def get_next_instance_by_class(class_label, dataset_dir):
    class_dir = os.path.join(dataset_dir, class_label)
    if not os.path.exists(class_dir):
        return None

    files = os.listdir(class_dir)
    random.shuffle(files)

    while len(files) > 0:
        next_instance = os.path.join(class_dir, files.pop())
        print(f"Следующий экземпляр класса '{class_label}': {next_instance}")

    print(f"Все экземпляры класса '{class_label}' закончились")


if __name__ == "__main__":
    dataset_dir = "D:\\Ucheba\\3 course\\PD\\lab2\\dataset"
    project_dir = "D:\\Ucheba\\3 course\\PD\\lab2"
    output_dir = "D:\\Ucheba\\3 course\\\PD\\lab3\\dataset"

    create_annotation_file(dataset_dir, project_dir)
    copy_dataset_with_new_names(dataset_dir, output_dir)
    create_dataset_with_random_names(dataset_dir, output_dir)

    class_label = 'bay_horse'
    get_next_instance_by_class(class_label, dataset_dir)


