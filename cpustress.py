import multiprocessing
import time
import math

def stress_test():
    # Perform a CPU intensive task
    x = 0
    while True:
        x += math.sqrt(12345 * 6789)

def run_stress_test(duration=60):
    # Get the number of CPU cores
    num_cores = multiprocessing.cpu_count()
    print(f"Starting stress test on {num_cores} CPU cores for {duration} seconds...")

    # Create a pool of worker processes equal to the number of CPU cores
    pool = multiprocessing.Pool(processes=num_cores)
    
    # Run the stress test for the specified duration
    pool.map_async(stress_test, range(num_cores))
    time.sleep(duration)

    # Terminate the pool and close processes after the duration
    pool.terminate()
    pool.join()
    print("CPU stress test completed.")

if __name__ == "__main__":
    # Run the CPU stress test for 60 seconds (you can change the duration)
    run_stress_test(duration=60)
