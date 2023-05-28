import concurrent.futures
import time

start=time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping....{seconds}'

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor: 
'''to switch to thread replace 'Process' to 'Thead' both are effecient 
but Thread is a bit faster then Process.'''
        secs=[5,4,3,2,1]
        results=[executor.submit(do_something,sec) for sec in secs ]
        for f in concurrent.futures.as_completed(results):
            print(f.result())

if __name__=='__main__':
    main()

finish=time.perf_counter()

print(f'Finished in {round(finish-start,2)} second(s)')