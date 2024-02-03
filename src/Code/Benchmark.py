import timeit

from src.Code.Recommendation.RecommendationSystem import BookRecommendationSystem


def query_function(query_system, query):
    """
    Executes a query on the provided query system.

    Args:
        query_system (BookRecommendationSystem): The book recommendation system to query.
        query (str): The query string to search for in the books.

    Returns:
        list: A list of books that match the query string.
    """
    return query_system.Query(query)


def time_query(system, query):
    """
    Measures the time it takes to execute a query on a given system.

    Args:
        system (BookRecommendationSystem): The book recommendation system to query.
        query (str): The query string to search for in the books.
    """
    number_of_runs = 100  # Adjust as needed
    duration = timeit.timeit(lambda: query_function(system, query), number=number_of_runs)

    average_time = duration / number_of_runs
    print(f"Average time for Query: {average_time:.4f} seconds")


def benchmark_query(systems):
    """
    Benchmarks the query function on multiple systems.

    Args:
        systems (list): A list of book recommendation systems to benchmark.
    """
    query = "The Great Grapes that went over the wall that one time"

    for i in range(len(systems)):
        print(f"Benchmarking system {i}")
        time_query(systems[i], query)
        print()


if __name__ == "__main__":
    """
    Main entry point of the script. Initializes the systems to test and benchmarks the query function on them.
    """
    systemsToTest = [BookRecommendationSystem()]
    benchmark_query(systemsToTest)
