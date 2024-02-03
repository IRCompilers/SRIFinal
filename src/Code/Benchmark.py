import timeit

from src.Code.Recommendation.RecommendationSystem import BookRecommendationSystem


def query_function(query_system, query):
    return query_system.Query(query)


def time_query(system, query):


    number_of_runs = 100  # Adjust as needed
    duration = timeit.timeit(lambda: query_function(system, query), number=number_of_runs)

    average_time = duration / number_of_runs
    print(f"Average time for Query: {average_time:.4f} seconds")


def benchmark_query(systems):
    query = "The Great Grapes that went over the wall that one time"

    for i in range(len(systems)):
        print(f"Benchmarking system {i}")
        time_query(systems[i], query)
        print()


if __name__ == "__main__":
    systemsToTest = [BookRecommendationSystem()]
    benchmark_query(systemsToTest)
