def common(status, messages, additional_info=None):
    return {
        "status": status,
        "data": dict(
            {"messages": messages},
            **({} if additional_info is None else {"additional_information": additional_info})
        )
    }
