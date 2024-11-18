import uvicorn
from multiprocessing import Process

def start_score_service():
    uvicorn.run("app.score_service:app", host="127.0.0.1", port=8001, reload=True)

def start_auth_service():
    uvicorn.run("app.auth_service:app", host="127.0.0.1", port=8002, reload=True)

def start_composition_service():
    uvicorn.run("app.composition_service:app", host="127.0.0.1", port=8003, reload=True)

if __name__ == "__main__":
    p1 = Process(target=start_score_service)
    p2 = Process(target=start_auth_service)
    p3 = Process(target=start_composition_service)

    p1.start()
    p2.start()
    p3.start()

    try:
        p1.join()
        p2.join()
        p3.join()
    except KeyboardInterrupt:
        p1.terminate()
        p2.terminate()
        p3.terminate()
        print("Good bye...")