import queue

queue = queue.Queue()

def generate_request(id):
    queue.put(id)

def process_request():
    if not queue.empty():
        queue.get()
    else:
        print("Queue is empty. No requests to process.")


def main():
    request_id = 0
    try:
        while True:
            generate_request(request_id)
            process_request()
            request_id += 1
            
    except KeyboardInterrupt:
        print("\nRequest processing system stopped.")


if __name__ == "__main__":
    main()