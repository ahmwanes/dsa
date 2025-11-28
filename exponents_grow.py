def get_follower_prediction(
    follower_count: int, influencer_type: str, num_months: int
) -> int:
    """
    While the influencers who use our platform are really great at taking selfies, most aren't super great at math. We need to write a tool that predicts an influencer's follower growth over time.

    Complete the get_follower_prediction function. It takes a follower_count integer, an influencer_type string and a num_months integer, and returns an integer.

    Calculate the number of followers an influencer will have after however many months according to the influencer type:

    "fitness": follower count quadruples each month
    "cosmetic": follower count triples each month
    other: follower count doubles each month
    For example, if a "fitness" influencer starts with 10 followers, then after 1 month they would have 40 followers. After 2 months, they would have 160 followers, and so on.

    Use the following geometric sequence formula that's slightly modified for this problem:

    total = a1 * r^n
    """
    if influencer_type == "fitness":
        return follower_count * (4**num_months)
    elif influencer_type == "cosmetic":
        return follower_count * (3**num_months)
    else:
        return follower_count * (2**num_months)


def get_influencer_score(num_followers, average_engagement_percentage) -> int:
    """Let's create an "influencer score". It will be a small number (like less than 100) that will give influencers a metric for comparing their social media success against their peers.

    Complete the get_influencer_score function. An influencer score is their average engagement percentage multiplied by log base 2 of their follower count."""
    import math

    return round(math.log(num_followers, 2) * average_engagement_percentage)


def num_possible_orders(num_posts):
    """
    Calculate the number of possible orders for a given number of posts.

    Args:
        num_posts (int): The number of posts.

    Returns:
        int: The number of possible orders.
    """
    if num_posts == 1:
        return 1
    return num_posts * num_possible_orders(num_posts - 1)


def decayed_followers(
    intl_followers: int, fraction_lost_daily: float, days: int
) -> int:
    """
    Calculate the number of followers an influencer will have after a certain number of days, given a daily fraction of followers lost.

    Args:
        intl_followers (int): The initial number of followers.
        fraction_lost_daily (float): The fraction of followers lost each day.
        days (int): The number of days to calculate the decayed followers for.

    Returns:
        int: The number of followers after the specified number of days.
    """
    retention_rate = 1 - fraction_lost_daily
    remaining = intl_followers * (retention_rate**days)
    return int(remaining)


def log_scale(data: list[int], base: int) -> list[int]:
    """
    In some cases, data can span several orders of magnitude, making it difficult to visualize on a linear scale.
    A logarithmic scale can help by compressing the data so that it's easier to understand.

    For example, at LockedIn we have influencers with follower counts ranging from 1 to 1,000,000,000.
    If we want to plot the follower count of each influencer on a graph, it would be difficult to see the differences between the smaller follower counts.
    We can use a logarithmic scale to compress the data so that it's easier to visualize.

    Args:
        data (list[int]): The data to be scaled.
        base (int): The base of the logarithm.

    Returns:
        list[int]: The scaled data.
    """
    import math

    scale = []

    for num in data:
        s = math.log(num, base)
        scale.append(round(s))

    return scale
