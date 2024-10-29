import requests
import argparse

def main():
    parser = argparse.ArgumentParser(description="AI-Powered Code Review Tool")
    parser.add_argument('--code', type=str, help="Code to review")
    args = parser.parse_args()

    # API Call
    response = requests.post('http://127.0.0.1:5000/review', json={"code": args.code})
    print(response.json())

if __name__ == "__main__":
    main()
