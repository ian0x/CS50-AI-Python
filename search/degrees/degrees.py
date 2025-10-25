import csv
import sys

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """
    
    """
    Frontier: Quaue of nodes (state=person_id, parent = previous node / None, action= (movie_id, person_id))
    Explored: Set of person_ids to check in case already explored
    0- Create initial node 
    1- Init frontier with source node
    2- Init explored set as empty
    3- Loop while frontier not empty
        a- Remove node from frontier
        b- If node state is target, then we found the path, reconstruct and return
        c- Add node state to explored
    """
    
    #If source and target are equals (same person), return empty path
    if source == target:
        return []

    #Use QueueFrontier for BFS search
    frontier = QueueFrontier()
    # Init collection of explored persons (state)
    explored_persons = set()

    #Start node and add to frontier
    first_node = Node(state=source, parent=None, action=None)
    frontier.add(first_node)

    while not frontier.empty():
        
        # Remove a node from the frontier
        current_node = frontier.remove()
        
        #Add current_node.state to explored_persons
        explored_persons.add(current_node.state)
        
        #Get neighbors 
        neighbors = neighbors_for_person(current_node.state)
        
        for movie_id, person_id in neighbors:
            #If person in explored_persons continue
            if person_id in explored_persons:
                continue
            
            #If node is in frontier
            if frontier.contains_state(person_id):
                continue
            
            #Create new node
            new_node = Node(
                state=person_id,
                parent=current_node,
                action=(movie_id,person_id)
            )
            
            #Check if we reached the target
            if person_id == target:
                path = []
                goal_node = new_node
                while goal_node.parent is not None:
                    path.append(goal_node.action)
                    goal_node = goal_node.parent
                path.reverse()
                return path
            
            #Add new node to frontier
            frontier.add(new_node)
        
    #Return None, no path found
    return None
            


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
