import sys
import json
import urllib.request
import urllib.error

def fetch_activity(username):

    url = f"https://api.github.com/users/{username}/events"
    
    try:
        # FIX 2: It is urllib.request (no 's')
        # FIX 3: Added 'with' keyword
        with urllib.request.urlopen(url) as response:
            # FIX 4: Spelling 'decode' correctly
            data = json.loads(response.read().decode('utf-8'))
            return data
            
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error: User '{username}' not found.")
        elif e.code == 403:
            print("Error: Rate limit exceeded. Try again later.")
        else:
            print(f"Error: API returned status code {e.code}")
        return None
    except urllib.error.URLError as e:
        print(f"Error: Network problem. ({e.reason})")
        return None

def format_event(event):
 
    event_type = event['type']
    repo_name = event['repo']['name']

    if event_type == "PushEvent":
   
        count = len(event['payload']['commits'])
        return f"Pushed {count} commits to {repo_name}"
        
  
    elif event_type == "WatchEvent":
        return f"Starred {repo_name}"
        
    elif event_type == "ForkEvent":
        return f"Forked {repo_name}"
        
    elif event_type == "CreateEvent":
     
        ref_type = event['payload']['ref_type']
        return f"Created {ref_type} in {repo_name}"
        
    elif event_type == "PullRequestEvent":
        action = event['payload']['action']
        return f"{action.capitalize()} a pull request in {repo_name}"
        
    else:
        return f"{event_type} in {repo_name}"

def main():
    if len(sys.argv) < 2:
        print("Usage: python github_activity.py <username>")
        return

    username = sys.argv[1]
    
    events = fetch_activity(username)
    
    if not events:
        return

    for event in events:
        try:
            message = format_event(event)
            print(f"- {message}")
        except KeyError:
            continue

if __name__ == "__main__":
    main()

              




