def question_answer(query, results, threshold=0.15):

    if not results:
        return (
            "I could not find enough support for that answer "
            "in the provided documents.",
            []
        )

    relevant_results = [
        result
        for result in results
        if result["score"] >= threshold
    ]

    if not relevant_results:
        return (
            "I could not find enough support for that answer "
            "in the provided documents.",
            []
        )

    best_result = relevant_results[0]

    answer = best_result["text"]

    sources = []

    for result in relevant_results:

        if result["source"] not in sources:
            sources.append(result["source"])

    return answer, sources