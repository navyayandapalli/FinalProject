import os
import time

# Function to generate a large file
def write_large_file(filename, size_in_mb):
    with open(filename, 'wb') as f:
        # Write random data to the file
        f.write(os.urandom(size_in_mb * 1024 * 1024))  # size_in_mb converted to bytes

# Function to read the large file
def read_large_file(filename):
    with open(filename, 'rb') as f:
        f.read()

# Function to perform the disk stress test
def disk_stress_test(file_size_mb, iterations):
    test_filename = "stress_test_file.dat"

    for i in range(iterations):
        print(f"Iteration {i+1} of {iterations}: Writing {file_size_mb} MB to disk...")
        write_large_file(test_filename, file_size_mb)

        print(f"Iteration {i+1}: Reading {file_size_mb} MB from disk...")
        read_large_file(test_filename)

        print(f"Iteration {i+1}: Deleting the file...")
        os.remove(test_filename)

        time.sleep(1)  # Optional: Add a small delay between iterations

    print("Disk stress test completed successfully.")

if __name__ == "__main__":
    # Adjust the parameters below as needed
    file_size = 100  # Size of the file to write in MB
    num_iterations = 10  # Number of times to perform write/read operations

    disk_stress_test(file_size, num_iterations)
