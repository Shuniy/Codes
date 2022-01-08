# Time : O(d) // Depth of deeper of two descendants
# Space : O(1) // Few While Loops

def get_descendant_depth(descendant, top_ancestor):
    depth = 0
    while descendant != top_ancestor:
        depth += 1
        descendant = descendant.ancestor
    return depth

def get_youngest_common_ancestor(top_ancestor, descendant_one, descendent_two):
    depth_one = get_descendant_depth(descendant_one, top_ancestor)
    depth_two = get_descendant_depth(descendent_two, top_ancestor)

    if depth_one > depth_two:
        return back_track_ancestral_tree(descendant_one, descendent_two, depth_one - depth_two)

    else:
        return back_track_ancestral_tree(descendent_two, descendant_one, depth_two - depth_one)

def back_track_ancestral_tree(lower_descendant, higher_descendant, diff):
    while diff > 0:
        lower_descendant = lower_descendant.ancestor
        diff -= 1
    while lower_descendant != higher_descendant:
        lower_descendant = lower_descendant.ancestor
        higher_descendant = higher_descendant.ancestor

    return lower_descendant