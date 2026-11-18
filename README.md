# Coding interview practice

Find interview practice by the technique used in each implementation. Historical solutions are for learning and reference; some are incomplete or incorrect. Syntax checks and a few examples do **not** establish general correctness.

## Navigate by pattern

Each solution has one primary location. Secondary techniques appear in the index without duplicate files. Standalone data structures live beside the relevant problems. Bundled graph exercises keep their helpers, notebooks and datasets together.

| Pattern | Material |
| --- | --- |
| [arrays and hashing](patterns/arrays_and_hashing/) | Scans, counting, maps, string and matrix manipulation |
| [two pointers](patterns/two_pointers/) | Opposing pointers, fast/slow pointers, sorted-array scans |
| [sliding window](patterns/sliding_window/) | Fixed and variable windows |
| [prefix sum](patterns/prefix_sum/) | Running sums, prefix/suffix products and submatrix sums |
| [binary search](patterns/binary_search/) | Ordered search and binary search on an answer |
| [sorting](patterns/sorting/) | Sorting, partition selection and merge-based exercises |
| [linked lists](patterns/linked_lists/) | List operations and implementations, including a queue built on a list |
| [stacks and queues](patterns/stacks_and_queues/) | Stack/queue operations, expression parsing and implementations |
| [monotonic stack](patterns/monotonic_stack/) | Next greater/smaller, stock span, histogram and binary-matrix rectangles |
| [monotonic queue](patterns/monotonic_queue/) | Sliding maximum attempts using ordered queues/deques |
| [heaps and priority queues](patterns/heaps_and_priority_queues/) | Top-k, streaming medians, Huffman coding and heap implementations |
| [intervals](patterns/intervals/) | Merging, overlap, scheduling and substring-range merging |
| [trees and bst](patterns/trees_and_bst/) | Tree traversals, search trees, ancestors and tree implementations |
| [tries](patterns/tries/) | Prefix/suffix lookup, autocomplete and routing |
| [graphs](patterns/graphs/) | Traversal, topology, paths, connectivity and spanning trees; bundled A-star examples |
| [recursion](patterns/recursion/) | Recursive demonstrations and un-memoized recursive solutions |
| [backtracking](patterns/backtracking/) | Choice enumeration, subsets, permutations, constraint search |
| [greedy](patterns/greedy/) | Local-choice solutions, including mixed greedy/DP variants |
| [dynamic programming](patterns/dynamic_programming/) | Memoization, tabulation and related approaches retained together |
| [bit manipulation](patterns/bit_manipulation/) | Bit operations and binary representations |
| [math and number theory](patterns/math_and_number_theory/) | Arithmetic, combinatorics, primes, geometry and sampling |

## Suggested revision order

1. Arrays and hashing → two pointers → sliding window → prefix sums.
2. Binary search → sorting → linked lists → stacks and queues.
3. Monotonic stacks/queues → heaps → intervals.
4. Trees and BSTs → tries → graph traversal, topology, paths and connectivity.
5. Recursion → backtracking → greedy → dynamic programming.
6. Bit manipulation and math; revisit weak patterns with another implementation.

## Run practice

Use Python 3.10 or newer from the repository root. Most algorithm scripts stand alone; many contain embedded examples or assertions.

```sh
python3 patterns/binary_search/binary_search.py
python3 patterns/dynamic_programming/coin_change.py
python3 patterns/linked_lists/queue_using_doubly_linked_list.py
```

The first two run their existing assertions. The queue uses a sibling import, so run it by file path. The existing tree-inversion unittest can be run with:

```sh
python3 -m unittest discover -s patterns/trees_and_bst -p 'invert_binary_tree.py'
```

That test currently fails; see [validation and existing issues](docs/validation.md). There is no repository-wide test runner.

Compile Java files separately to avoid collisions between unrelated exercise classes. Public classes and existing package declarations follow their new paths:

```sh
mkdir -p /tmp/interview_java
javac -d /tmp/interview_java patterns/sliding_window/longest_substring_without_repeating_characters.java
java -cp /tmp/interview_java patterns.sliding_window.longest_substring_without_repeating_characters
```

For the C++ A-star example, run from its data directory:

```sh
cd patterns/graphs/a_star_grid
clang++ -std=c++17 a_star_search.cpp -o /tmp/interview_a_star
/tmp/interview_a_star
```

The route-planner notebook and harness run from [their own folder](patterns/graphs/route_planner/). They require `networkx`, Plotly and notebook dependencies; the historical helper uses the obsolete `plotly.plotly` API. The self-contained `route_planner_local.py` example avoids these dependencies. Existing map fixtures remain in that bundle; notebook imports and data references follow the renamed files.

## Projects and language exercises

[projects/](projects/) contains [Tkinter and Turtle applications](projects/tkinter/), [telephone-record CSV exercises](projects/telephone_records/), [machine-learning exercises](projects/machine_learning/) and a [job-scheduler exercise](projects/job_scheduler/). Run applications and CSV scripts from their own directory so relative assets and data paths resolve. The GUI projects retain their images, data and sibling modules. Their optional dependencies include pandas and pyperclip; they were not launched during verification.

[language_fundamentals/](language_fundamentals/) contains Java object-oriented language exercises, C++ pointers/references/memory, Python closures and pattern printing, and Swift/Xcode snippets. The local machine-learning environment is ignored by Git and is not a dependency specification.

The [move manifest](docs/reorganisation_manifest.csv) accounts for every original tracked path and authored local file, including identical copies consolidated into a single destination and the deletion already present before this work. [Historical search/sort explanations](docs/search_sort_explanations.md) are retained as written.

## Problem index

Expand a pattern to see every source file and available language variant. Names describe the retained implementations; entries marked “placeholder” remain unfinished. Helper modules and bundled datasets are linked with their exercise.

<details>
<summary>arrays and hashing (81 files)</summary>

| Problem / exercise | Solutions | Secondary patterns |
| --- | --- | --- |
| add one | [Python](patterns/arrays_and_hashing/add_one.py) | — |
| add upto k daily coding | [Python](patterns/arrays_and_hashing/add_upto_k_daily_coding.py) | — |
| anagram or not | [C++](patterns/arrays_and_hashing/anagram_or_not.cpp) | — |
| apartment hunting | [Python](patterns/arrays_and_hashing/apartment_hunting.py) | — |
| ascii value differences | [C++](patterns/arrays_and_hashing/ascii_value_differences.cpp) | — |
| bitonic subarray | [C++](patterns/arrays_and_hashing/bitonic_subarray.cpp) | — |
| caesar cipher encryptor | [Python](patterns/arrays_and_hashing/caesar_cipher_encryptor.py) | — |
| check permutation | [Python](patterns/arrays_and_hashing/check_permutation.py) | — |
| diagonal matrix | [C++](patterns/arrays_and_hashing/diagonal_matrix.cpp) | — |
| duplicate element limited array | [Python](patterns/arrays_and_hashing/duplicate_element_limited_array.py) | — |
| duplicate number | [Python](patterns/arrays_and_hashing/duplicate_number.py) | — |
| dynamic array | [Python](patterns/arrays_and_hashing/dynamic_array.py) | — |
| equilibrium brute force | [C++](patterns/arrays_and_hashing/equilibrium_brute_force.cpp) | — |
| find three largest number | [Python](patterns/arrays_and_hashing/find_three_largest_number.py) | — |
| flip the words | [Python](patterns/arrays_and_hashing/flip_the_words.py) | — |
| four number sum | [Python](patterns/arrays_and_hashing/four_number_sum.py) | [two pointers](patterns/two_pointers/) |
| generating subarrays | [C++](patterns/arrays_and_hashing/generating_subarrays.cpp) | — |
| group anagrams | [Python](patterns/arrays_and_hashing/group_anagrams.py) | — |
| hamming distance | [Python](patterns/arrays_and_hashing/hamming_distance.py) | — |
| hash map | [Python](patterns/arrays_and_hashing/hash_map.py) | — |
| is unique | [Python](patterns/arrays_and_hashing/is_unique.py) | — |
| knuth morris pratt | [Python](patterns/arrays_and_hashing/knuth_morris_pratt.py) | — |
| largest range | [Python](patterns/arrays_and_hashing/largest_range.py) | — |
| largest subarray equal zero one | [C++](patterns/arrays_and_hashing/largest_subarray_equal_zero_one.cpp) | — |
| largest subarray equal zero one brute force | [C++](patterns/arrays_and_hashing/largest_subarray_equal_zero_one_brute_force.cpp) | — |
| largest subarray equal zero one placeholder | [C++](patterns/arrays_and_hashing/largest_subarray_equal_zero_one_placeholder.cpp) | — |
| leaders in array | [C++](patterns/arrays_and_hashing/leaders_in_array.cpp) | — |
| leaders in array brute force | [C++](patterns/arrays_and_hashing/leaders_in_array_brute_force.cpp) | — |
| leaders in array right scan | [C++](patterns/arrays_and_hashing/leaders_in_array_right_scan.cpp) | — |
| longest nice substring | [Java](patterns/arrays_and_hashing/longest_nice_substring.java) | — |
| longest palindromic substring | [Python](patterns/arrays_and_hashing/longest_palindromic_substring.py) | — |
| lru cache | [Python](patterns/arrays_and_hashing/lru_cache.py) | [linked lists](patterns/linked_lists/) |
| lru cache ordered dict | [Python](patterns/arrays_and_hashing/lru_cache_ordered_dict.py) | — |
| majority element | [C++](patterns/arrays_and_hashing/majority_element.cpp) | — |
| majority element1 | [C++](patterns/arrays_and_hashing/majority_element1.cpp) | — |
| majority element2 | [C++](patterns/arrays_and_hashing/majority_element2.cpp) | — |
| maps | [Python](patterns/arrays_and_hashing/maps.py) | — |
| matrix wave traversal | [C++](patterns/arrays_and_hashing/matrix_wave_traversal.cpp) | — |
| max product two integers | [Python](patterns/arrays_and_hashing/max_product_two_integers.py) | — |
| min max | [Python](patterns/arrays_and_hashing/min_max_exercise.py) | — |
| missing element in unsorted hash | [C++](patterns/arrays_and_hashing/missing_element_in_unsorted_hash.cpp) | — |
| missing positive integer daily coding | [Python](patterns/arrays_and_hashing/missing_positive_integer_daily_coding.py) | — |
| multiple missing elements sorted | [C++](patterns/arrays_and_hashing/multiple_missing_elements_sorted.cpp) | — |
| pair sum problem | [Python](patterns/arrays_and_hashing/pair_sum_problem.py) | — |
| pair sum to target | [Python](patterns/arrays_and_hashing/pair_sum_to_target.py) | — |
| pair with given sum | [Python](patterns/arrays_and_hashing/pair_with_given_sum.py) | — |
| pairs with ascii value difference k | [C++](patterns/arrays_and_hashing/pairs_with_ascii_value_difference_k.cpp) | — |
| palindrome permutation | [Python](patterns/arrays_and_hashing/palindrome_permutation.py) | — |
| pattern matcher placeholder | [Python](patterns/arrays_and_hashing/pattern_matcher_placeholder.py) | — |
| printing pairs | [Python](patterns/arrays_and_hashing/printing_pairs.py) | — |
| printing subarrays | [Python](patterns/arrays_and_hashing/printing_subarrays.py) | — |
| product two integers | [C++](patterns/arrays_and_hashing/product_two_integers.cpp) | — |
| rainwater tapping | [C++](patterns/arrays_and_hashing/rainwater_tapping.cpp) | — |
| rectangle mania | [Python](patterns/arrays_and_hashing/rectangle_mania.py) | — |
| rotate image 90 | [C++](patterns/arrays_and_hashing/rotate_image_90.cpp) | — |
| rotate image 90 and 180 | [C++](patterns/arrays_and_hashing/rotate_image_90_and_180.cpp) | — |
| rotate matrix | [Python](patterns/arrays_and_hashing/rotate_matrix.py) | — |
| rotated image | [Python](patterns/arrays_and_hashing/rotated_image.py) | — |
| rotated sorted array | [Python](patterns/arrays_and_hashing/rotated_sorted_array.py) | — |
| run length decoding | [Python](patterns/arrays_and_hashing/run_length_decoding.py) | — |
| run length encoding | [Python](patterns/arrays_and_hashing/run_length_encoding.py) | — |
| set matrix zeroes | [Python](patterns/arrays_and_hashing/set_matrix_zeroes.py) | — |
| shortest path directions | [Python](patterns/arrays_and_hashing/shortest_path_directions.py) | — |
| spiral form clockwise | [C++](patterns/arrays_and_hashing/spiral_form_clockwise.cpp) | — |
| spiral print | [Python](patterns/arrays_and_hashing/spiral_print.py) | — |
| stock prices | [Python](patterns/arrays_and_hashing/stock_prices.py) | — |
| string compression | [Python](patterns/arrays_and_hashing/string_compression.py) | — |
| string key hash table | [Python](patterns/arrays_and_hashing/string_key_hash_table.py) | — |
| string rotation | [Python](patterns/arrays_and_hashing/string_rotation.py) | — |
| subarray sort | [Python](patterns/arrays_and_hashing/subarray_sort.py) | — |
| subarrays | [Python](patterns/arrays_and_hashing/subarrays.py) | — |
| sum to k | [C++](patterns/arrays_and_hashing/sum_to_k.cpp) | — |
| trailing park problem | [Python](patterns/arrays_and_hashing/trailing_park_problem.py) | — |
| two number sum | [Python: two number](patterns/arrays_and_hashing/two_number.py) · [Python: two number sum](patterns/arrays_and_hashing/two_number_sum.py) | [two pointers](patterns/two_pointers/) |
| union and intersection | [Python](patterns/arrays_and_hashing/union_and_intersection.py) | [linked lists](patterns/linked_lists/) |
| unsorted integer array | [Python](patterns/arrays_and_hashing/unsorted_integer_array.py) | — |
| urlify | [Python](patterns/arrays_and_hashing/urlify.py) | — |
| water area | [Python](patterns/arrays_and_hashing/water_area.py) | — |
| zero matrix | [Python](patterns/arrays_and_hashing/zero_matrix.py) | — |
| zigzag traverse | [Python](patterns/arrays_and_hashing/zigzag_traverse.py) | — |

</details>

<details>
<summary>two pointers (38 files)</summary>

| Problem / exercise | Solutions | Secondary patterns |
| --- | --- | --- |
| compare backspace string | [Python](patterns/two_pointers/compare_backspace_string.py) | — |
| cycle circular array | [Python](patterns/two_pointers/cycle_circular_array.py) | — |
| detecting loops linked list | [Python](patterns/two_pointers/detecting_loops_linked_list.py) | [linked lists](patterns/linked_lists/) |
| dutch national flag | [Python](patterns/two_pointers/dutch_national_flag.py) | — |
| dutch national flag partition | [Python](patterns/two_pointers/dutch_national_flag_partition.py) | — |
| find loop | [Python](patterns/two_pointers/find_loop.py) | [linked lists](patterns/linked_lists/) |
| happy number | [Python](patterns/two_pointers/happy_number.py) | — |
| linked list cycle | [Python](patterns/two_pointers/linked_list_cycle.py) | [linked lists](patterns/linked_lists/) |
| loop detection | [Python](patterns/two_pointers/loop_detection.py) | [linked lists](patterns/linked_lists/) |
| loop detection pointer set | [C++](patterns/two_pointers/loop_detection_pointer_set.cpp) | [linked lists](patterns/linked_lists/) |
| merge two arrays | [Python](patterns/two_pointers/merge_two_arrays.py) | — |
| minimize equation | [Python](patterns/two_pointers/minimize_equation.py) | — |
| move element to end | [Python](patterns/two_pointers/move_element_to_end.py) | — |
| one away | [Python](patterns/two_pointers/one_away.py) | — |
| pair target sum | [Python](patterns/two_pointers/pair_target_sum.py) | — |
| palindrome check | [Python](patterns/two_pointers/palindrome_check.py) | — |
| palindrome check approaches | [Python](patterns/two_pointers/palindrome_check_approaches.py) | — |
| palindrome linked list | [Python](patterns/two_pointers/palindrome_linked_list.py) | [linked lists](patterns/linked_lists/) |
| rearrange linked list | [Python](patterns/two_pointers/rearrange_linked_list.py) | [linked lists](patterns/linked_lists/) |
| remove duplicates | [Python](patterns/two_pointers/remove_duplicates.py) | — |
| remove kth node from end | [Python](patterns/two_pointers/remove_kth_node_from_end.py) | [linked lists](patterns/linked_lists/) |
| remove nth node from end | [Python](patterns/two_pointers/remove_nth_node_from_end.py) | [linked lists](patterns/linked_lists/) |
| search 2d matrix | [Python](patterns/two_pointers/search_2d_matrix.py) | — |
| search in sorted matrix | [Python](patterns/two_pointers/search_in_sorted_matrix.py) | — |
| shortest window sort | [Python](patterns/two_pointers/shortest_window_sort.py) | — |
| smallest difference | [Python](patterns/two_pointers/smallest_difference.py) | — |
| sort 012 | [Python: dutch national flag sort 012](patterns/two_pointers/dutch_national_flag_sort_012.py) · [Python: sort 012 approaches](patterns/two_pointers/sort_012_approaches.py) · [Python: sort 012 exercise](patterns/two_pointers/sort_012_exercise.py) | — |
| sorted array search | [Python](patterns/two_pointers/sorted_array_search.py) | — |
| string reverse | [C++](patterns/two_pointers/string_reverse.cpp) | — |
| target sum pairs | [C++](patterns/two_pointers/target_sum_pairs.cpp) | — |
| three number sum | [Python: three number sum](patterns/two_pointers/three_number_sum.py) · [Python: three numbers](patterns/two_pointers/three_numbers.py) | — |
| triple sum close zero | [Python](patterns/two_pointers/triple_sum_close_zero.py) | — |
| triple sum zero | [Python](patterns/two_pointers/triple_sum_zero.py) | — |
| triplets smaller sum | [Python](patterns/two_pointers/triplets_smaller_sum.py) | — |
| unique quadruplets | [Python](patterns/two_pointers/unique_quadruplets.py) | — |

</details>

<details>
<summary>sliding window (50 files)</summary>

| Problem / exercise | Solutions | Secondary patterns |
| --- | --- | --- |
| binary subarrays with sum | [Java](patterns/sliding_window/binary_subarrays_with_sum.java) | — |
| contains duplicate | [Java](patterns/sliding_window/contains_duplicate.java) | [arrays and hashing](patterns/arrays_and_hashing/) |
| count occurrences anagrams | [Java](patterns/sliding_window/count_occurrences_anagrams.java) · [Python](patterns/sliding_window/count_occurrences_anagrams.py) | [arrays and hashing](patterns/arrays_and_hashing/) |
| find anagrams | [C++](patterns/sliding_window/find_anagrams.cpp) | [arrays and hashing](patterns/arrays_and_hashing/) |
| first negative number window size k | [Java](patterns/sliding_window/first_negative_number_window_size_k.java) · [Python](patterns/sliding_window/first_negative_number_window_size_k.py) | — |
| fruits in baskets | [C++](patterns/sliding_window/fruits_in_baskets.cpp) | [arrays and hashing](patterns/arrays_and_hashing/) |
| general format sliding window | [Python](patterns/sliding_window/general_format_sliding_window.py) | — |
| k beauty string | [Java](patterns/sliding_window/k_beauty_string.java) | — |
| largest subarray sum k | [Java](patterns/sliding_window/largest_subarray_sum_k.java) · [Python](patterns/sliding_window/largest_subarray_sum_k.py) | [prefix sum](patterns/prefix_sum/) |
| longest repeating character replacement | [Java](patterns/sliding_window/longest_repeating_character_replacement.java) · [C++](patterns/sliding_window/longest_substring_same_letters_after_replacement.cpp) | [arrays and hashing](patterns/arrays_and_hashing/) |
| longest subarray ones after replacement | [C++](patterns/sliding_window/longest_subarray_ones_after_replacement.cpp) | — |
| longest substring at least k repeating characters | [Java](patterns/sliding_window/longest_substring_at_least_k_repeating_characters.java) | [arrays and hashing](patterns/arrays_and_hashing/) |
| longest substring k distinct characters | [C++](patterns/sliding_window/longest_substring_k_distinct_characters.cpp) | [arrays and hashing](patterns/arrays_and_hashing/) |
| longest substring k unique characters | [Java](patterns/sliding_window/longest_substring_k_unique_characters.java) · [Python](patterns/sliding_window/longest_substring_k_unique_characters.py) | [arrays and hashing](patterns/arrays_and_hashing/) |
| longest substring of all vowels order | [Java](patterns/sliding_window/longest_substring_of_all_vowels_order.java) | [arrays and hashing](patterns/arrays_and_hashing/) |
| longest substring with k characters daily coding | [Python](patterns/sliding_window/longest_substring_with_k_characters_daily_coding.py) | [arrays and hashing](patterns/arrays_and_hashing/) |
| longest substring without repeating characters | [Python: longest substring with no repeating characters](patterns/sliding_window/longest_substring_with_no_repeating_characters.py) · [Python: longest substring without duplication](patterns/sliding_window/longest_substring_without_duplication.py) · [Java](patterns/sliding_window/longest_substring_without_repeating_characters.java) · [Python: longest substring without repeating characters](patterns/sliding_window/longest_substring_without_repeating_characters.py) · [Python: longest substring without repetiton daily coding](patterns/sliding_window/longest_substring_without_repetiton_daily_coding.py) · [C++](patterns/sliding_window/no_repeat_substring.cpp) | [arrays and hashing](patterns/arrays_and_hashing/) |
| max consecutive ones3 | [Java](patterns/sliding_window/max_consecutive_ones3.java) | — |
| max subarray with size | [C++](patterns/sliding_window/max_subarray_with_size.cpp) | — |
| maximum average subarray i | [Java](patterns/sliding_window/maximum_average_subarray_i.java) | — |
| maximum sum subarray size k | [C++](patterns/sliding_window/maximum_sum_subarray_size_k.cpp) · [Java](patterns/sliding_window/maximum_sum_subarray_size_k.java) · [Python](patterns/sliding_window/maximum_sum_subarray_size_k.py) | — |
| minimum difference between highest lowest k scores | [Java](patterns/sliding_window/minimum_difference_between_highest_lowest_k_scores.java) | — |
| minimum recolors get k consecutive black blocks | [Java](patterns/sliding_window/minimum_recolors_get_k_consecutive_black_blocks.java) | — |
| minimum window substring | [Java](patterns/sliding_window/maximum_window_substring.java) · [Python: minimum window substring](patterns/sliding_window/minimum_window_substring.py) · [Python: smallest substring containing](patterns/sliding_window/smallest_substring_containing.py) · [C++](patterns/sliding_window/smallest_window_substring.cpp) · [Python: string window](patterns/sliding_window/string_window.py) | [arrays and hashing](patterns/arrays_and_hashing/) |
| number substrings containing all three characters | [Java](patterns/sliding_window/number_substrings_containing_all_three_characters.java) | [arrays and hashing](patterns/arrays_and_hashing/) |
| permutation string | [C++](patterns/sliding_window/permutation_string.cpp) | — |
| pick toys | [Python](patterns/sliding_window/pick_toys.py) | — |
| smallest subarray with sum | [C++](patterns/sliding_window/smallest_subarray_with_sum.cpp) | — |
| subarray with given sum | [C++](patterns/sliding_window/subarray_with_given_sum.cpp) | — |
| subarray with sum | [C++](patterns/sliding_window/subarray_with_sum.cpp) | — |
| subarrays distinct elements | [Python](patterns/sliding_window/subarrays_distinct_elements.py) | — |
| subarrays k different integers | [Java](patterns/sliding_window/subarrays_k_different_integers.java) | — |
| substrings size3 distinct characters | [Java](patterns/sliding_window/substrings_size3_distinct_characters.java) | [arrays and hashing](patterns/arrays_and_hashing/) |
| words concatenation | [C++](patterns/sliding_window/words_concatenation.cpp) | [arrays and hashing](patterns/arrays_and_hashing/) |

</details>

<details>
<summary>prefix sum (11 files)</summary>

| Problem / exercise | Solutions | Secondary patterns |
| --- | --- | --- |
| divisible sub arrays | [Python](patterns/prefix_sum/divisible_sub_arrays.py) | — |
| equilibrium point | [C++](patterns/prefix_sum/equilibrium_point.cpp) | — |
| equilibrium running sum | [C++](patterns/prefix_sum/equilibrium_running_sum.cpp) | — |
| left right sum differences | [Java](patterns/prefix_sum/left_right_sum_differences.java) | — |
| max length subarray equal 0 1 | [Python](patterns/prefix_sum/max_length_subarray_equal_0_1.py) | — |
| max length subarray given sum | [Python](patterns/prefix_sum/max_length_subarray_given_sum.py) | — |
| product of all numbers | [C++](patterns/prefix_sum/product_of_all_numbers.cpp) | — |
| product other than num daily coding | [Python](patterns/prefix_sum/product_other_than_num_daily_coding.py) | — |
| subarray sums | [Python](patterns/prefix_sum/subarray_sums.py) | — |
| subarray with 0 sum exists or not | [Python](patterns/prefix_sum/subarray_with_0_sum_exists_or_not.py) | — |
| sum of elements in submatrix | [C++](patterns/prefix_sum/sum_of_elements_in_submatrix.cpp) | — |

</details>

<details>
<summary>binary search (35 files)</summary>

| Problem / exercise | Solutions | Secondary patterns |
| --- | --- | --- |
| allocate minimum number pages | [Python](patterns/binary_search/allocate_minimum_number_pages.py) | — |
| binary search | [Python](patterns/binary_search/binary_search.py) | — |
| binary search first and last indices | [Python](patterns/binary_search/binary_search_first_and_last_indices.py) | — |
| binary search placeholder | [Python](patterns/binary_search/binary_search_placeholder.py) | — |
| binary search practice | [Python](patterns/binary_search/binary_search_practice.py) | — |
| binary search recursive iterative and linear | [Python](patterns/binary_search/binary_search_recursive_iterative_and_linear.py) | — |
| binary search reverse | [Python](patterns/binary_search/binary_search_reverse.py) | — |
| ceil element sorted array | [Python](patterns/binary_search/ceil_element_sorted_array.py) | — |
| count occurrences element | [Python](patterns/binary_search/count_occurrences_element.py) | — |
| element sorted rotated array | [Python](patterns/binary_search/element_sorted_rotated_array.py) | — |
| first last occurrence array | [Python](patterns/binary_search/first_last_occurrence_array.py) | — |
| floor element sorted array | [Python](patterns/binary_search/floor_element_sorted_array.py) | — |
| index first 1 infinite sorted array | [Python](patterns/binary_search/index_first_1_infinite_sorted_array.py) | — |
| max element bitonic array | [Python](patterns/binary_search/max_element_bitonic_array.py) | — |
| median sorted array | [Python](patterns/binary_search/median_sorted_array.py) | — |
| minimum difference element | [Python](patterns/binary_search/minimum_difference_element.py) | — |
| missing element in sorted array | [C++](patterns/binary_search/missing_element_in_sorted_array.cpp) | — |
| next alphabetical element | [Python](patterns/binary_search/next_alphabetical_element.py) | — |
| order not known search agnostic | [Python](patterns/binary_search/order_not_known_search_agnostic.py) | — |
| peak element | [Python](patterns/binary_search/peak_element.py) | — |
| position element infinite sorted array | [Python](patterns/binary_search/position_element_infinite_sorted_array.py) | — |
| rotated array search | [C++](patterns/binary_search/rotated_array_search.cpp) · [Python: rotated array search](patterns/binary_search/rotated_array_search.py) · [Python: rotated array search exercise](patterns/binary_search/rotated_array_search_exercise.py) | — |
| search element bitonic array | [Python](patterns/binary_search/search_element_bitonic_array.py) | — |
| search for range | [Python](patterns/binary_search/search_for_range.py) | — |
| search in rotated sorted array | [Python](patterns/binary_search/search_in_rotated_sorted_array.py) | — |
| search methods | [C++](patterns/binary_search/search_methods.cpp) | — |
| search nearly sorted array | [Python](patterns/binary_search/search_nearly_sorted_array.py) | — |
| shifted binary search | [Python](patterns/binary_search/shifted_binary_search.py) | — |
| square root | [Python](patterns/binary_search/square_root_exercise.py) | — |
| square root of an integer | [Python](patterns/binary_search/square_root_of_an_integer.py) | — |
| times array rotated | [Python](patterns/binary_search/times_array_rotated.py) | — |
| two sum2 | [Python](patterns/binary_search/two_sum2.py) | — |
| variation on binary search | [Python](patterns/binary_search/variation_on_binary_search.py) | — |

</details>

<details>
<summary>sorting (48 files)</summary>

| Problem / exercise | Solutions | Secondary patterns |
| --- | --- | --- |
| arrange numbers to form given number | [C++](patterns/sorting/arrange_numbers_to_form_given_number.cpp) | — |
| bubble sort | [C++](patterns/sorting/bubble_sort.cpp) · [Python: bubble sort](patterns/sorting/bubble_sort.py) · [Python: bubble sort annotated approaches](patterns/sorting/bubble_sort_annotated_approaches.py) · [Python: bubble sort iterative and recursive](patterns/sorting/bubble_sort_iterative_and_recursive.py) | — |
| bucket sort | [Python: bucket sort](patterns/sorting/bucket_sort.py) · [Python: bucket sort annotated](patterns/sorting/bucket_sort_annotated.py) | — |
| closest pair of points 1 d | [Python](patterns/sorting/closest_pair_of_points_1_d.py) | [recursion](patterns/recursion/) |
| closest pair of points 2 d | [Python](patterns/sorting/closest_pair_of_points_2_d.py) | [recursion](patterns/recursion/) |
| counting inversion | [Python](patterns/sorting/counting_inversion.py) | — |
| counting inversions | [Python](patterns/sorting/counting_inversions.py) | — |
| counting sort | [Python](patterns/sorting/counting_sort.py) | — |
| counting specific sorting of string | [Python](patterns/sorting/counting_specific_sorting_of_string.py) | — |
| cycle sort | [Python](patterns/sorting/cycle_sort.py) | — |
| heap sort | [Python: heap sort](patterns/sorting/heap_sort.py) · [Python: heap sort annotated](patterns/sorting/heap_sort_annotated.py) · [Python: heap sort annotated exercise](patterns/sorting/heap_sort_annotated_exercise.py) · [Python: heap sort incremental exercise](patterns/sorting/heap_sort_incremental_exercise.py) | [heaps and priority queues](patterns/heaps_and_priority_queues/) |
| insertion sort | [C++](patterns/sorting/insertion_sort.cpp) · [Python: insertion sort](patterns/sorting/insertion_sort.py) · [Python: insertion sort annotated approaches](patterns/sorting/insertion_sort_annotated_approaches.py) · [Python: insertion sort shifting](patterns/sorting/insertion_sort_shifting.py) | — |
| longest consecutive subsequence | [Python](patterns/sorting/longest_consecutive_subsequence.py) | — |
| merge sort | [Python: merge sort](patterns/sorting/merge_sort.py) · [Python: merge sort annotated approaches](patterns/sorting/merge_sort_annotated_approaches.py) · [Python: merge sort annotated exercise](patterns/sorting/merge_sort_annotated_exercise.py) · [Python: merge sort exercise](patterns/sorting/merge_sort_exercise.py) · [Python: merge sort index ranges](patterns/sorting/merge_sort_index_ranges.py) | [recursion](patterns/recursion/) |
| merge two sorted arrays | [Python](patterns/sorting/merge_two_sorted_arrays.py) | — |
| quick select | [Python](patterns/sorting/quick_select.py) | — |
| quick sort | [Python: quick sort](patterns/sorting/quick_sort.py) · [Python: quick sort partition approaches](patterns/sorting/quick_sort_partition_approaches.py) · [Python: quick sort pivot exercise](patterns/sorting/quick_sort_pivot_exercise.py) | [recursion](patterns/recursion/) |
| quick sort lomuto | [Python](patterns/sorting/quick_sort_lomuto_annotated.py) | [recursion](patterns/recursion/) |
| radix sort | [Python: radix sort](patterns/sorting/radix_sort.py) · [Python: radix sort annotated](patterns/sorting/radix_sort_annotated.py) | — |
| rearrange digits | [Python: rearrange digits exercise](patterns/sorting/rearrange_digits_exercise.py) · [Python: rearrange digits merge sort](patterns/sorting/rearrange_digits_merge_sort.py) | [recursion](patterns/recursion/) |
| selection sort | [C++](patterns/sorting/selection_sort.cpp) · [Python: selection sort](patterns/sorting/selection_sort.py) · [Python: selection sort annotated approaches](patterns/sorting/selection_sort_annotated_approaches.py) · [Python: selection sort swapping](patterns/sorting/selection_sort_swapping.py) | — |
| shell sort | [C++](patterns/sorting/shell_sort.cpp) · [Python: shell sort](patterns/sorting/shell_sort.py) · [Python: shell sort annotated approaches](patterns/sorting/shell_sort_annotated_approaches.py) | — |
| sort binary array linear time | [Python](patterns/sorting/sort_binary_array_linear_time.py) | — |
| string sort | [Python](patterns/sorting/string_sort.py) | — |
| wave sort single array | [C++](patterns/sorting/wave_sort_single_array.cpp) | — |

</details>

<details>
<summary>linked lists (34 files)</summary>

| Problem / exercise | Solutions | Secondary patterns |
| --- | --- | --- |
| add two numbers linked list daily coding | [Python](patterns/linked_lists/add_two_numbers_linked_list_daily_coding.py) | — |
| block chain | [Python](patterns/linked_lists/block_chain.py) | — |
| circular linked list | [Python](patterns/linked_lists/circular_linked_list.py) | — |
| delete middle node | [Python](patterns/linked_lists/delete_middle_node.py) | — |
| doubly linked list | [Python](patterns/linked_lists/doubly_linked_list.py) | — |
| doubly linked list with initial items | [Python](patterns/linked_lists/doubly_linked_list_with_initial_items.py) | — |
| even after odd | [Python](patterns/linked_lists/even_after_odd.py) | — |
| flattening linked list | [C++](patterns/linked_lists/flattening_linked_list.cpp) | — |
| flattening nested linked list | [Python](patterns/linked_lists/flattening_nested_linked_list.py) | — |
| insertion at beginning linked list | [C++](patterns/linked_lists/insertion_at_beginning_linked_list.cpp) | — |
| insertion at end linked list | [C++](patterns/linked_lists/insertion_at_end_linked_list.cpp) | — |
| insertion at position linked list | [C++](patterns/linked_lists/insertion_at_position_linked_list.cpp) | — |
| intersection | [Python](patterns/linked_lists/intersection.py) | — |
| kth from last placeholder | [Python](patterns/linked_lists/kth_from_last_placeholder.py) | — |
| linked list | [C++](patterns/linked_lists/linked_list.cpp) · [Python](patterns/linked_lists/linked_list.py) | — |
| linked list construction | [Python](patterns/linked_lists/linked_list_construction.py) | — |
| linked list creation | [Python](patterns/linked_lists/linked_list_creation_exercise.py) | — |
| linked list practice | [Python](patterns/linked_lists/linked_list_practice.py) | — |
| merge k sorted lists daily coding | [Python](patterns/linked_lists/merge_k_sorted_lists_daily_coding.py) | [sorting](patterns/sorting/) |
| merge linked list | [Python](patterns/linked_lists/merge_linked_list.py) | — |
| palindrome | [Python](patterns/linked_lists/palindrome.py) | — |
| partition | [Python](patterns/linked_lists/partition.py) | — |
| queue using doubly linked list | [Python](patterns/linked_lists/queue_using_doubly_linked_list.py) | [stacks and queues](patterns/stacks_and_queues/) |
| quick sort linked list daily coding | [Python](patterns/linked_lists/quick_sort_linked_list_daily_coding.py) | [sorting](patterns/sorting/) |
| remove duplicate linked list | [Python](patterns/linked_lists/remove_duplicate_linked_list.py) | — |
| reverse linked list | [C++](patterns/linked_lists/reverse_linked_list.cpp) · [Python: reverse linked list](patterns/linked_lists/reverse_linked_list.py) · [Python: reverse linked list insert at head](patterns/linked_lists/reverse_linked_list_insert_at_head.py) | — |
| skip and delete | [Python](patterns/linked_lists/skip_and_delete.py) | — |
| sum lists | [Python](patterns/linked_lists/sum_lists.py) | — |
| swap nodes | [Python](patterns/linked_lists/swap_nodes.py) | — |
| types of linked lists | [Python](patterns/linked_lists/types_of_linked_lists.py) | — |
| xor linked list daily coding | [Python](patterns/linked_lists/xor_linked_list_daily_coding.py) | — |

</details>

<details>
<summary>stacks and queues (36 files)</summary>

| Problem / exercise | Solutions | Secondary patterns |
| --- | --- | --- |
| animal shelter | [Python](patterns/stacks_and_queues/animal_shelter.py) | — |
| balanced brackets | [Python: balanced bracket](patterns/stacks_and_queues/balanced_bracket.py) · [Python: balanced brackets](patterns/stacks_and_queues/balanced_brackets.py) | — |
| balanced parenthesis | [Python](patterns/stacks_and_queues/balanced_parenthesis.py) | — |
| circular queue | [C++](patterns/stacks_and_queues/circular_queue.cpp) · [Python](patterns/stacks_and_queues/circular_queue.py) | — |
| decimal binary | [Python](patterns/stacks_and_queues/decimal_binary.py) | — |
| infix to postfix | [C++](patterns/stacks_and_queues/infix_to_postfix.cpp) · [Python](patterns/stacks_and_queues/infix_to_postfix.py) | — |
| infix to prefix | [Python](patterns/stacks_and_queues/infix_to_prefix.py) | — |
| iterative toh | [Python](patterns/stacks_and_queues/iterative_toh.py) | — |
| last n order ids daily coding | [Python](patterns/stacks_and_queues/last_n_order_ids_daily_coding.py) | — |
| min max stack | [Python: min max stack](patterns/stacks_and_queues/min_max_stack.py) · [Python: min max stack construction](patterns/stacks_and_queues/min_max_stack_construction.py) | — |
| min stack | [Python](patterns/stacks_and_queues/min_stack.py) | — |
| minimum bracket reversal | [Python](patterns/stacks_and_queues/minimum_bracket_reversal.py) | — |
| pop array stack | [C++](patterns/stacks_and_queues/pop_array_stack.cpp) | — |
| queue | [C++](patterns/stacks_and_queues/queue.cpp) | — |
| queue array | [Python](patterns/stacks_and_queues/queue_array.py) | — |
| queue linked list | [C++](patterns/stacks_and_queues/queue_linked_list.cpp) · [Python](patterns/stacks_and_queues/queue_linked_list.py) | — |
| queue using stack | [Python](patterns/stacks_and_queues/queue_using_stack.py) | — |
| queue with stacks | [Python](patterns/stacks_and_queues/queue_with_stacks.py) | — |
| reverse polish notation | [Python](patterns/stacks_and_queues/reverse_polish_notation.py) | — |
| reverse queue | [Python](patterns/stacks_and_queues/reverse_queue.py) | — |
| reverse stack | [Python](patterns/stacks_and_queues/reverse_stack.py) | — |
| single array to three stacks | [Python](patterns/stacks_and_queues/single_array_to_three_stacks.py) | — |
| sort stack | [Python](patterns/stacks_and_queues/sort_stack.py) | — |
| stack | [Python](patterns/stacks_and_queues/stack.py) | — |
| stack array | [Python](patterns/stacks_and_queues/stack_array.py) | — |
| stack linked list | [C++](patterns/stacks_and_queues/stack_linked_list.cpp) · [Python](patterns/stacks_and_queues/stack_linked_list.py) | — |
| stack min | [Python](patterns/stacks_and_queues/stack_min.py) | — |
| stack of plates | [Python](patterns/stacks_and_queues/stack_of_plates.py) | — |
| stack using queues | [Python](patterns/stacks_and_queues/stack_using_queues.py) | — |
| stacks | [C++](patterns/stacks_and_queues/stacks.cpp) | — |

</details>

<details>
<summary>monotonic stack (7 files)</summary>

| Problem / exercise | Solutions | Secondary patterns |
| --- | --- | --- |
| max area rectangle binary matrix | [Python](patterns/monotonic_stack/max_area_rectangle_binary_matrix.py) | [arrays and hashing](patterns/arrays_and_hashing/) |
| maximum area histogram | [Python](patterns/monotonic_stack/maximum_area_histogram.py) | [arrays and hashing](patterns/arrays_and_hashing/) |
| nearest greater left | [Python](patterns/monotonic_stack/nearest_greater_left.py) | [arrays and hashing](patterns/arrays_and_hashing/) |
| nearest greater right next largest element | [Python](patterns/monotonic_stack/nearest_greater_right_next_largest_element.py) | [arrays and hashing](patterns/arrays_and_hashing/) |
| nearest smaller left | [Python](patterns/monotonic_stack/nearest_smaller_left.py) | [arrays and hashing](patterns/arrays_and_hashing/) |
| nearest smaller right next smallest element | [Python](patterns/monotonic_stack/nearest_smaller_right_next_smallest_element.py) | [arrays and hashing](patterns/arrays_and_hashing/) |
| stock span problem | [Python](patterns/monotonic_stack/stock_span_problem.py) | [arrays and hashing](patterns/arrays_and_hashing/) |

</details>

<details>
<summary>monotonic queue (3 files)</summary>

| Problem / exercise | Solutions | Secondary patterns |
| --- | --- | --- |
| maximum all subarrays size k | [Java](patterns/monotonic_queue/maximum_all_subarrays_size_k.java) · [Python: maximum all subarrays size k](patterns/monotonic_queue/maximum_all_subarrays_size_k.py) · [Python: maximum values in subarrays daily coding](patterns/monotonic_queue/maximum_values_in_subarrays_daily_coding.py) | [sliding window](patterns/sliding_window/) |

</details>

<details>
<summary>heaps and priority queues (18 files)</summary>

| Problem / exercise | Solutions | Secondary patterns |
| --- | --- | --- |
| closest numbers | [Python](patterns/heaps_and_priority_queues/closest_numbers.py) | — |
| connect ropes to minimize cost | [Python](patterns/heaps_and_priority_queues/connect_ropes_to_minimize_cost.py) | [greedy](patterns/greedy/) |
| continuous median | [Python: continuos median](patterns/heaps_and_priority_queues/continuos_median.py) · [Python: continuous median](patterns/heaps_and_priority_queues/continuous_median.py) | — |
| frequency sort | [Python](patterns/heaps_and_priority_queues/frequency_sort.py) | — |
| heap | [Python: heap](patterns/heaps_and_priority_queues/heap.py) · [Python: heaps](patterns/heaps_and_priority_queues/heaps.py) | — |
| heaps capacity | [Python](patterns/heaps_and_priority_queues/heaps_capacity_exercise.py) | — |
| hostel visit | [Python](patterns/heaps_and_priority_queues/hostel_visit.py) | — |
| huffman | [C++](patterns/heaps_and_priority_queues/huffman.cpp) | [greedy](patterns/greedy/) |
| huffman coding | [Python](patterns/heaps_and_priority_queues/huffman_coding.py) | [greedy](patterns/greedy/) |
| k closest point origin | [Python](patterns/heaps_and_priority_queues/k_closest_point_origin.py) | — |
| k largest element | [Python](patterns/heaps_and_priority_queues/k_largest_element.py) | — |
| kth smallest element | [Python](patterns/heaps_and_priority_queues/kth_smallest_element.py) | — |
| min heap construction | [Python](patterns/heaps_and_priority_queues/min_heap_construction.py) | — |
| sort k sorted array | [Python](patterns/heaps_and_priority_queues/sort_k_sorted_array.py) | — |
| sum k1 elements k2 elements | [Python](patterns/heaps_and_priority_queues/sum_k1_elements_k2_elements.py) | — |
| top k frequent elements | [Python](patterns/heaps_and_priority_queues/top_k_frequent_elements.py) | — |

</details>

<details>
<summary>intervals (9 files)</summary>

| Problem / exercise | Solutions | Secondary patterns |
| --- | --- | --- |
| calendar matching placeholder | [Python](patterns/intervals/calendar_matching_placeholder.py) | — |
| conflicting appointments | [Python](patterns/intervals/conflicting_appointments.py) | — |
| employee free time | [Python](patterns/intervals/employee_free_time.py) | [heaps and priority queues](patterns/heaps_and_priority_queues/) |
| insert interval | [Python](patterns/intervals/insert_interval.py) | — |
| maximum cpu load | [Python](patterns/intervals/maximum_cpu_load.py) | [heaps and priority queues](patterns/heaps_and_priority_queues/) |
| merge intervals | [Python](patterns/intervals/merge_intervals.py) | — |
| min platforms | [Python](patterns/intervals/min_platforms.py) | — |
| minimum meeting rooms | [Python](patterns/intervals/minimum_meeting_rooms.py) | [heaps and priority queues](patterns/heaps_and_priority_queues/) |
| underscorify substring | [Python](patterns/intervals/underscorify_substring.py) | — |

</details>

<details>
<summary>trees and bst (38 files)</summary>

| Problem / exercise | Solutions | Secondary patterns |
| --- | --- | --- |
| active directory | [Python](patterns/trees_and_bst/active_directory.py) | — |
| avl tree | [Python](patterns/trees_and_bst/avl_tree.py) | — |
| binary tree | [C++](patterns/trees_and_bst/binary_tree.cpp) · [Python](patterns/trees_and_bst/binary_tree.py) | — |
| binary tree stub | [Python](patterns/trees_and_bst/binary_tree_stub.py) | — |
| branch sums | [Python](patterns/trees_and_bst/branch_sums.py) | [recursion](patterns/recursion/) |
| breadth first tree traversal | [Python](patterns/trees_and_bst/breadth_first_tree_traversal.py) | [recursion](patterns/recursion/) |
| bst | [Python](patterns/trees_and_bst/bst.py) | — |
| bst construction | [Python](patterns/trees_and_bst/bst_construction.py) | — |
| bst construction iterative | [Python](patterns/trees_and_bst/bst_construction_iterative.py) | — |
| bst construction recursive | [Python](patterns/trees_and_bst/bst_construction_recursive.py) | [recursion](patterns/recursion/) |
| bst delete | [Python](patterns/trees_and_bst/bst_delete.py) | — |
| bst traversal | [Python](patterns/trees_and_bst/bst_traversal.py) | [recursion](patterns/recursion/) |
| bst with parent pointers | [Python](patterns/trees_and_bst/bst_with_parent_pointers.py) | — |
| closest value bst | [Python](patterns/trees_and_bst/closest_value_bst.py) | — |
| depth first tree traversal | [Python](patterns/trees_and_bst/depth_first_tree_traversal.py) | [recursion](patterns/recursion/) |
| diameter binary tree | [Python](patterns/trees_and_bst/diameter_binary_tree.py) | — |
| find closest value in bst | [Python](patterns/trees_and_bst/find_closest_value_in_bst.py) | — |
| height of binary tree | [Python](patterns/trees_and_bst/height_of_binary_tree.py) | — |
| invert binary tree | [Python](patterns/trees_and_bst/invert_binary_tree.py) | — |
| iterative in order traversal | [Python](patterns/trees_and_bst/iterative_in_order_traversal.py) | [recursion](patterns/recursion/) |
| iterative inorder traversal | [Python](patterns/trees_and_bst/iterative_inorder_traversal.py) | [recursion](patterns/recursion/) |
| longest absolute path daily coding | [Python](patterns/trees_and_bst/longest_absolute_path_daily_coding.py) | — |
| lowest common manager | [Python](patterns/trees_and_bst/lowest_common_manager.py) | — |
| max path sum | [Python](patterns/trees_and_bst/max_path_sum.py) | [recursion](patterns/recursion/) |
| max path sum in binary tree | [Python](patterns/trees_and_bst/max_path_sum_in_binary_tree.py) | [recursion](patterns/recursion/) |
| node depth | [Python](patterns/trees_and_bst/node_depth.py) | [recursion](patterns/recursion/) |
| path root to node | [Python](patterns/trees_and_bst/path_root_to_node.py) | — |
| red black bst | [Python](patterns/trees_and_bst/red_black_bst.py) | — |
| red black tree | [Python](patterns/trees_and_bst/red_black_tree.py) | — |
| same bsts | [Python](patterns/trees_and_bst/same_bsts.py) | — |
| serialize root daily coding | [Python](patterns/trees_and_bst/serialize_root_daily_coding.py) | — |
| tree and queue exercises | [Notebook](patterns/trees_and_bst/tree_and_queue_exercises.ipynb) | — |
| tree list representation | [Python](patterns/trees_and_bst/tree_list_representation.py) | — |
| trees | [Python](patterns/trees_and_bst/trees.py) | — |
| universal trees daily coding | [Python](patterns/trees_and_bst/universal_trees_daily_coding.py) | — |
| validate bst | [Python](patterns/trees_and_bst/validate_bst.py) | — |
| youngest common ancestor | [Python](patterns/trees_and_bst/youngest_common_ancestor.py) | [recursion](patterns/recursion/) |

</details>

<details>
<summary>tries (12 files)</summary>

| Problem / exercise | Solutions | Secondary patterns |
| --- | --- | --- |
| autocomplete | [Notebook](patterns/tries/autocomplete_exercise.ipynb) · [Python](patterns/tries/autocomplete_with_tries.py) | [recursion](patterns/recursion/) |
| http router | [Python: http router exercise](patterns/tries/http_router_exercise.py) · [Python: http router using a trie](patterns/tries/http_router_using_a_trie.py) | — |
| multi string search | [Python](patterns/tries/multi_string_search.py) | — |
| return possible strings daily coding | [Python](patterns/tries/return_possible_strings_daily_coding.py) | — |
| suffix tree compressed edges | [Python](patterns/tries/suffix_tree_compressed_edges.py) | — |
| suffix trie | [Python](patterns/tries/suffix_trie.py) | — |
| suffix trie construction | [Python](patterns/tries/suffix_trie_construction.py) | — |
| tries | [Python: tries](patterns/tries/tries.py) · [Python: tries annotated exercise](patterns/tries/tries_annotated_exercise.py) | — |
| tries using default dict | [Python](patterns/tries/tries_using_default_dict.py) | — |

</details>

<details>
<summary>graphs (51 files)</summary>

| Problem / exercise | Solutions | Secondary patterns |
| --- | --- | --- |
| a star search | [C++](patterns/graphs/a_star_grid/a_star_search.cpp) | — |
| adjacency list | [Python](patterns/graphs/adjacency_list.py) | — |
| adjacency matrix | [Python](patterns/graphs/adjacency_matrix.py) | — |
| airport connections | [Python](patterns/graphs/airport_connections.py) | [greedy](patterns/greedy/) |
| bellman ford | [C++](patterns/graphs/bellman_ford.cpp) · [Python](patterns/graphs/bellman_ford.py) | — |
| bfs | [Python](patterns/graphs/bfs.py) | — |
| breadth first search | [Python](patterns/graphs/breadth_first_search.py) | — |
| cheapest flights k stops | [Python](patterns/graphs/cheapest_flights_k_stops.py) | — |
| connecting islands | [Python](patterns/graphs/connecting_islands.py) | — |
| course schedule2 | [Python](patterns/graphs/course_schedule2.py) | — |
| cycle detection | [Python](patterns/graphs/cycle_detection.py) | — |
| cycle detection directed | [Python](patterns/graphs/cycle_detection_directed.py) | — |
| depth first search | [Python](patterns/graphs/depth_first_search.py) | — |
| dfs | [Python](patterns/graphs/dfs.py) | — |
| dfs placeholder | [C++](patterns/graphs/dfs_placeholder.cpp) | — |
| dijkstra | [C++](patterns/graphs/dijkstra.cpp) · [Python](patterns/graphs/dijkstra.py) | [heaps and priority queues](patterns/heaps_and_priority_queues/) |
| dijkstras algo | [Python](patterns/graphs/dijkstras_algo.py) | [heaps and priority queues](patterns/heaps_and_priority_queues/) |
| disjoint sets | [Python](patterns/graphs/disjoint_sets.py) | — |
| eventual safe states | [Python](patterns/graphs/eventual_safe_states.py) | — |
| find path exists | [Python](patterns/graphs/find_path_exists.py) | — |
| flood fill | [Python](patterns/graphs/flood_fill.py) | — |
| floyd warshalls | [Python](patterns/graphs/floyd_warshalls.py) | — |
| geeks village wells | [Python](patterns/graphs/geeks_village_wells.py) | — |
| graph adjacency matrix | [Python](patterns/graphs/graph_adjacency_matrix.py) | — |
| graph bfs | [Python](patterns/graphs/graph_bfs.py) | — |
| graph dfs | [Python](patterns/graphs/graph_dfs.py) | — |
| graph dfs recursive | [Python](patterns/graphs/graph_dfs_recursive.py) | — |
| kruskals algo | [Python](patterns/graphs/kruskals_algo.py) | [greedy](patterns/greedy/) |
| largest color value | [Python](patterns/graphs/largest_color_value.py) | — |
| longest cycle | [Python](patterns/graphs/longest_cycle.py) | — |
| make connected | [Python](patterns/graphs/make_connected.py) | — |
| number islands | [Python](patterns/graphs/number_islands.py) | — |
| path minimum effort | [Python](patterns/graphs/path_minimum_effort.py) | [heaps and priority queues](patterns/heaps_and_priority_queues/) |
| prims algorithm | [Python](patterns/graphs/prims_algorithm.py) | [heaps and priority queues](patterns/heaps_and_priority_queues/) |
| reorder path zero | [Python](patterns/graphs/reorder_path_zero.py) | — |
| river sizes | [Python](patterns/graphs/river_sizes.py) | — |
| rotting oranges | [Python](patterns/graphs/rotting_oranges.py) | — |
| route between nodes placeholder | [Python](patterns/graphs/route_between_nodes_placeholder.py) | — |
| route planner | [Python](patterns/graphs/route_planner/route_planner.py) | [heaps and priority queues](patterns/heaps_and_priority_queues/) |
| route planner helpers | [Python](patterns/graphs/route_planner/helpers.py) | — |
| route planner local | [Python](patterns/graphs/route_planner/route_planner_local.py) | [heaps and priority queues](patterns/heaps_and_priority_queues/) |
| route planner notebook | [Notebook](patterns/graphs/route_planner/route_planner_notebook.ipynb) | [heaps and priority queues](patterns/heaps_and_priority_queues/) |
| route planner tests | [Python](patterns/graphs/route_planner/route_planner_tests.py) | [heaps and priority queues](patterns/heaps_and_priority_queues/) |
| single cycle check | [Python](patterns/graphs/single_cycle_check.py) | — |
| snakes ladders | [Python](patterns/graphs/snakes_ladders.py) | — |
| steps knight | [Python](patterns/graphs/steps_knight.py) | — |
| topological sort | [Python: topological sort dfs edges](patterns/graphs/topological_sort_dfs_edges.py) · [Python: topological sort job graph](patterns/graphs/topological_sort_job_graph.py) · [Python: topological sort kahn](patterns/graphs/topological_sort_kahn.py) | — |

</details>

<details>
<summary>recursion (58 files)</summary>

| Problem / exercise | Solutions | Secondary patterns |
| --- | --- | --- |
| call stack | [Python](patterns/recursion/call_stack.py) | — |
| check palindrome | [Python](patterns/recursion/check_palindrome.py) | — |
| check palindrome recurse | [C++](patterns/recursion/check_palindrome_recurse.cpp) | — |
| deep reverse | [C++](patterns/recursion/deep_reverse.cpp) · [Python](patterns/recursion/deep_reverse.py) | — |
| delete middle element of stack | [Python](patterns/recursion/delete_middle_element_of_stack.py) | — |
| delete middle of stack | [Python](patterns/recursion/delete_middle_of_stack.py) | — |
| exponent recursion | [C++](patterns/recursion/exponent_recursion.cpp) | — |
| factorial | [C++](patterns/recursion/factorial.cpp) · [Java](patterns/recursion/factorial.java) · [Python: factorial digit array](patterns/recursion/factorial_digit_array.py) · [Python: factorial recursive iterative and digits](patterns/recursion/factorial_recursive_iterative_and_digits.py) | — |
| fibonacci | [C++](patterns/recursion/fibonacci.cpp) | — |
| fibonacci recursive | [Java](patterns/recursion/fibonacci_recursive.java) | — |
| fibonacci series | [Java](patterns/recursion/fibonacci_series.java) | — |
| file recursion | [Python](patterns/recursion/file_recursion.py) | — |
| find index recurse | [C++](patterns/recursion/find_index_recurse.cpp) | — |
| first occurrence | [Python](patterns/recursion/first_occurrence.py) | — |
| furthest building | [Python](patterns/recursion/furthest_building.py) | — |
| increase decrease numbers | [C++](patterns/recursion/increase_decrease_numbers.cpp) | — |
| josephus problem | [Python](patterns/recursion/josephus_problem.py) | — |
| kth grammar | [Python](patterns/recursion/kth_grammar.py) | — |
| kth symbol grammar | [Python](patterns/recursion/kth_symbol_grammar.py) | — |
| last index recursion | [Python](patterns/recursion/last_index_recursion.py) | — |
| last occurrence | [Python](patterns/recursion/last_occurrence.py) | — |
| mapping decoding daily coding | [Python](patterns/recursion/mapping_decoding_daily_coding.py) | — |
| matrix chain multiplication | [Python](patterns/recursion/matrix_chain_multiplication.py) · [C++](patterns/recursion/matrix_chain_multiplication_naive.cpp) | — |
| minimum number insertion deletion from a to b | [Python](patterns/recursion/minimum_number_insertion_deletion_from_a_to_b.py) | — |
| minimum operations to reduce x to zero | [Python](patterns/recursion/minimum_operations_to_reduce_x_to_zero.py) | — |
| natural sum expression fragment | [C++](patterns/recursion/natural_sum_expression_fragment.cpp) | — |
| power | [Python](patterns/recursion/power.py) | — |
| print 1 to n | [Python](patterns/recursion/print_1_to_n.py) | — |
| print n to 1 | [Python](patterns/recursion/print_n_to_1.py) | — |
| product sum | [Python](patterns/recursion/product_sum.py) | — |
| recursion directions | [Python](patterns/recursion/recursion_directions.py) | — |
| reverse stack | [Python](patterns/recursion/reverse_stack.py) | — |
| reverse stack recursion | [Python](patterns/recursion/reverse_stack_recursion.py) | — |
| reverse string | [Python](patterns/recursion/reverse_string.py) | — |
| reverse string recurse | [C++](patterns/recursion/reverse_string_recurse.cpp) | — |
| scrambled string | [Python](patterns/recursion/scrambled_string.py) | — |
| sort a stack | [Python](patterns/recursion/sort_a_stack.py) | — |
| sort an array using recursion | [Python](patterns/recursion/sort_an_array_using_recursion.py) | — |
| sort array recursion | [Python](patterns/recursion/sort_array_recursion.py) | — |
| sort stack recursion | [Python](patterns/recursion/sort_stack_recursion.py) | — |
| sorted array check | [Python](patterns/recursion/sorted_array_check.py) | — |
| staircase | [Python: staircase](patterns/recursion/staircase.py) · [Python: staircase annotated](patterns/recursion/staircase_annotated.py) | — |
| staircase recurse | [C++](patterns/recursion/staircase_recurse.cpp) | — |
| subarray | [Python](patterns/recursion/subarray.py) | — |
| substring | [Python](patterns/recursion/substring.py) | — |
| sum of natural numbers recursion | [C++](patterns/recursion/sum_of_natural_numbers_recursion.cpp) | — |
| taylor series recursion | [C++](patterns/recursion/taylor_series_recursion.cpp) | — |
| tower of hanoi | [C++](patterns/recursion/tower_of_hanoi.cpp) · [Python: tower of hanoi](patterns/recursion/tower_of_hanoi.py) · [Python: tower of hanoi exercise](patterns/recursion/tower_of_hanoi_exercise.py) | — |
| validate subsequence | [Python](patterns/recursion/validate_subsequence.py) | — |
| wiggle subsequence | [Python](patterns/recursion/wiggle_subsequence.py) | — |

</details>

<details>
<summary>backtracking (47 files)</summary>

| Problem / exercise | Solutions | Secondary patterns |
| --- | --- | --- |
| binary prefix more ones than zeroes | [Python](patterns/backtracking/binary_prefix_more_ones_than_zeroes.py) | — |
| binary prefix more ones than zeroes helper | [Python](patterns/backtracking/binary_prefix_more_ones_than_zeroes_helper.py) | — |
| boggle board placeholder | [Python](patterns/backtracking/boggle_board_placeholder.py) | [graphs](patterns/graphs/) |
| case change recursion | [Python](patterns/backtracking/case_change_recursion.py) | — |
| combination | [Python](patterns/backtracking/combination.py) | — |
| combination with repetition with k | [Python](patterns/backtracking/combination_with_repetition_with_k.py) | — |
| combinations | [Python](patterns/backtracking/combinations.py) | — |
| generate all balanced parenthesis | [Python](patterns/backtracking/generate_all_balanced_parenthesis.py) | — |
| generate balanced parenthesis | [Python](patterns/backtracking/generate_balanced_parenthesis.py) | — |
| generating subsequences | [C++](patterns/backtracking/generating_subsequences.cpp) | — |
| graph coloring | [Python](patterns/backtracking/graph_coloring.py) | [graphs](patterns/graphs/) |
| keypad combinations | [Python](patterns/backtracking/keypad_combinations.py) | — |
| large number k swaps | [Python](patterns/backtracking/large_number_k_swaps.py) | — |
| letter case permutation | [Python](patterns/backtracking/letter_case_permutation.py) | — |
| list permutation recurse | [C++](patterns/backtracking/list_permutation_recurse.cpp) | — |
| list permutations | [Python](patterns/backtracking/list_permutations.py) | — |
| n digit numbers increasing | [Python](patterns/backtracking/n_digit_numbers_increasing.py) | — |
| n queens | [Python](patterns/backtracking/n_queens.py) | — |
| permutation | [Python: permutation](patterns/backtracking/permutation.py) · [Python: permutation visited swap and repetition](patterns/backtracking/permutation_visited_swap_and_repetition.py) | — |
| permutation letter case | [Python](patterns/backtracking/permutation_letter_case.py) | — |
| permutation strings | [Python](patterns/backtracking/permutation_strings.py) | — |
| permutation with case change | [Python](patterns/backtracking/permutation_with_case_change.py) | — |
| permutation with repetition | [Python](patterns/backtracking/permutation_with_repetition.py) | — |
| permutation with spaces | [Python](patterns/backtracking/permutation_with_spaces.py) | — |
| permutation with spaces helper | [Python](patterns/backtracking/permutation_with_spaces_helper.py) | — |
| permutations | [Python](patterns/backtracking/permutations.py) | — |
| permutations of string | [C++](patterns/backtracking/permutations_of_string.cpp) | — |
| phone keypad problem | [Python](patterns/backtracking/phone_keypad_problem.py) | — |
| phone number combinations | [C++](patterns/backtracking/phone_number_combinations.cpp) | — |
| possible palindromic partitions | [Python](patterns/backtracking/possible_palindromic_partitions.py) | — |
| powerset | [Python: powerset](patterns/backtracking/powerset.py) · [Python: powerset bitmask](patterns/backtracking/powerset_bitmask.py) · [Python: powerset iterative and recursive](patterns/backtracking/powerset_iterative_and_recursive.py) | [bit manipulation](patterns/bit_manipulation/) |
| rat in maze | [Python](patterns/backtracking/rat_in_maze.py) | [graphs](patterns/graphs/) |
| return codes | [Python](patterns/backtracking/return_codes.py) | — |
| return subsets | [Python](patterns/backtracking/return_subsets.py) | — |
| staircase problem daily coding | [Python](patterns/backtracking/staircase_problem_daily_coding.py) | — |
| string permutation | [Python](patterns/backtracking/string_permutation.py) | — |
| subsequence | [Python](patterns/backtracking/subsequence.py) | — |
| subsequences | [Python: subsequences](patterns/backtracking/subsequences.py) · [Python: subsequences recursive and bitmask](patterns/backtracking/subsequences_recursive_and_bitmask.py) | [bit manipulation](patterns/bit_manipulation/) |
| subsets | [Python](patterns/backtracking/subsets_bitmask.py) | [bit manipulation](patterns/bit_manipulation/) |
| subsets recursion | [Python](patterns/backtracking/subsets_recursion.py) | — |
| sudoku solver | [Python](patterns/backtracking/sudoku_solver.py) | — |
| unique subsets | [Python](patterns/backtracking/unique_subsets.py) | — |
| word break 2 | [Python](patterns/backtracking/word_break_2.py) | — |

</details>

<details>
<summary>greedy (16 files)</summary>

| Problem / exercise | Solutions | Secondary patterns |
| --- | --- | --- |
| best time buy sell stock ii | [Java](patterns/greedy/best_time_buy_sell_stock_ii.java) | — |
| can place flowers | [Java](patterns/greedy/can_place_flowers.java) | — |
| candy | [Java](patterns/greedy/candy.java) | — |
| chewbacca | [C++](patterns/greedy/chewbacca.cpp) | — |
| gas station | [Java](patterns/greedy/gas_station.java) | — |
| hand of straights | [Java](patterns/greedy/hand_of_straights.java) | [heaps and priority queues](patterns/heaps_and_priority_queues/) |
| jump game | [Java](patterns/greedy/jump_game.java) | — |
| jump game ii | [Java](patterns/greedy/jump_game_ii.java) | — |
| largest number k swaps | [Python](patterns/greedy/largest_number_k_swaps.py) | [heaps and priority queues](patterns/heaps_and_priority_queues/) |
| largest number k swaps n numbers | [Python](patterns/greedy/largest_number_k_swaps_n_numbers.py) | — |
| lemonade change | [Java](patterns/greedy/lemonade_change.java) | — |
| min number of jumps | [Python](patterns/greedy/min_number_of_jumps.py) | [dynamic programming](patterns/dynamic_programming/) |
| min rewards | [Python](patterns/greedy/min_rewards.py) | — |
| minimum sum four digit number after splitting digits | [Java](patterns/greedy/minimum_sum_four_digit_number_after_splitting_digits.java) | — |
| remove duplicate letters | [Java](patterns/greedy/remove_duplicate_letters.java) | [monotonic stack](patterns/monotonic_stack/) |
| wiggle subsequence | [Java](patterns/greedy/wiggle_subsequence.java) | — |

</details>

<details>
<summary>dynamic programming (65 files)</summary>

| Problem / exercise | Solutions | Secondary patterns |
| --- | --- | --- |
| best time buy sell stock | [Java](patterns/dynamic_programming/best_time_buy_sell_stock.java) | — |
| binary trees cameras | [Python](patterns/dynamic_programming/binary_trees_cameras.py) | [trees and bst](patterns/trees_and_bst/) |
| climb stairs | [Python](patterns/dynamic_programming/climb_stairs.py) | — |
| coin change | [Python](patterns/dynamic_programming/coin_change.py) | — |
| coin change problem1 | [Python](patterns/dynamic_programming/coin_change_problem1.py) | — |
| coin change problem2 | [Python](patterns/dynamic_programming/coin_change_problem2.py) | — |
| count subsets with given difference | [Python](patterns/dynamic_programming/count_subsets_with_given_difference.py) | — |
| count subsets with given sum | [Python](patterns/dynamic_programming/count_subsets_with_given_sum.py) | — |
| disk stacking | [Python](patterns/dynamic_programming/disk_stacking.py) | — |
| egg dropping problem | [Python](patterns/dynamic_programming/egg_dropping_problem.py) | [recursion](patterns/recursion/) |
| equal sum partition | [Python](patterns/dynamic_programming/equal_sum_partition.py) | — |
| evaluate expression boolean parenthesization | [Python](patterns/dynamic_programming/evaluate_expression_boolean_parenthesization.py) | — |
| fibonacci | [Python](patterns/dynamic_programming/fibonacci_recursive_memo_tabulation.py) | [recursion](patterns/recursion/) |
| house robber | [Python](patterns/dynamic_programming/house_robber.py) | — |
| interweaving strings | [Python](patterns/dynamic_programming/interweaving_strings.py) | — |
| kadane | [Python: kadane](patterns/dynamic_programming/kadane.py) · [Python: kadane algorithm](patterns/dynamic_programming/kadane_algorithm.py) · [Python: kadanes algorithm](patterns/dynamic_programming/kadanes_algorithm.py) · [Python: maximum sub array sum](patterns/dynamic_programming/maximum_sub_array_sum.py) | — |
| knapsack problem | [Python](patterns/dynamic_programming/knapsack_problem.py) | — |
| knapsack value table | [Python](patterns/dynamic_programming/knapsack_value_table.py) | — |
| largest sum non adjacent numbers daily coding | [Python](patterns/dynamic_programming/largest_sum_non_adjacent_numbers_daily_coding.py) | — |
| levenshtein distance | [Python](patterns/dynamic_programming/levenshtein_distance.py) | — |
| longest common subsequence | [C++](patterns/dynamic_programming/longest_common_subsequence.cpp) · [Python: longest common subsequence](patterns/dynamic_programming/longest_common_subsequence.py) · [Python: longest common subsequence length](patterns/dynamic_programming/longest_common_subsequence_length.py) · [Python: longest common subsequence recursive memo tabulation](patterns/dynamic_programming/longest_common_subsequence_recursive_memo_tabulation.py) | [recursion](patterns/recursion/) |
| longest common substring | [Python](patterns/dynamic_programming/longest_common_substring.py) | — |
| longest increasing subsequence | [Python](patterns/dynamic_programming/longest_increasing_subsequence.py) | — |
| longest palindromic subsequence | [Python: longest palindromic sequence](patterns/dynamic_programming/longest_palindromic_sequence.py) · [Python: longest palindromic subsequence](patterns/dynamic_programming/longest_palindromic_subsequence.py) | — |
| longest repeating subsequence | [Python](patterns/dynamic_programming/longest_repeating_subsequence.py) | — |
| longest string chain | [Python](patterns/dynamic_programming/longest_string_chain.py) | — |
| matrix chain multiplication | [C++](patterns/dynamic_programming/matrix_chain_multiplication.cpp) · [Python: matrix chain multiplication memo](patterns/dynamic_programming/matrix_chain_multiplication_memo.py) · [Python: matrix chain multiplication tabulation](patterns/dynamic_programming/matrix_chain_multiplication_tabulation.py) | [recursion](patterns/recursion/) |
| max profit with k transactions | [Python](patterns/dynamic_programming/max_profit_with_k_transactions.py) | — |
| max subset sum no adjacent | [Python: max subset sum no adjacent](patterns/dynamic_programming/max_subset_sum_no_adjacent.py) · [Python: maximum subset sum with no adjacent element](patterns/dynamic_programming/maximum_subset_sum_with_no_adjacent_element.py) | — |
| max sum increasing subsequence | [Python](patterns/dynamic_programming/max_sum_increasing_subsequence.py) | — |
| maximum subarray circular | [C++](patterns/dynamic_programming/maximum_subarray_circular.cpp) | — |
| maximum subarrays sum | [C++](patterns/dynamic_programming/maximum_subarrays_sum.cpp) | — |
| min number of coins for change | [Python: min number of coins for change](patterns/dynamic_programming/min_number_of_coins_for_change.py) · [Python: minimum number of coins for change](patterns/dynamic_programming/minimum_number_of_coins_for_change.py) | — |
| min operations | [Python](patterns/dynamic_programming/min_operations.py) | — |
| minimum number deletion string palindrome | [Python](patterns/dynamic_programming/minimum_number_deletion_string_palindrome.py) | — |
| minimum number insertion palindrome | [Python](patterns/dynamic_programming/minimum_number_insertion_palindrome.py) | — |
| minimum subset sum difference | [Python](patterns/dynamic_programming/minimum_subset_sum_difference.py) | — |
| nth fibonacci | [Python](patterns/dynamic_programming/nth_fibonacci.py) | — |
| number of binary tree topologies | [Python: number of binary tree topologies](patterns/dynamic_programming/number_of_binary_tree_topologies.py) · [Python: number of possible binary tree topologies](patterns/dynamic_programming/number_of_possible_binary_tree_topologies.py) | [trees and bst](patterns/trees_and_bst/) |
| number of ways to make change | [Python: number of ways to make change](patterns/dynamic_programming/number_of_ways_to_make_change.py) · [Python: number of ways to make changes](patterns/dynamic_programming/number_of_ways_to_make_changes.py) | — |
| numbers in pi | [Python](patterns/dynamic_programming/numbers_in_pi.py) | — |
| optimal binary search tree | [C++](patterns/dynamic_programming/optimal_binary_search_tree.cpp) | [trees and bst](patterns/trees_and_bst/) |
| palindrome partitioning | [Python](patterns/dynamic_programming/palindrome_partitioning.py) | — |
| palindrome partitioning min cuts | [Python](patterns/dynamic_programming/palindrome_partitioning_min_cuts.py) | — |
| rod cutting | [Python](patterns/dynamic_programming/rod_cutting.py) | — |
| sequence pattern matching | [Python](patterns/dynamic_programming/sequence_pattern_matching.py) | — |
| shortest common supersequence | [Python](patterns/dynamic_programming/shortest_common_supersequence.py) | — |
| subset sum | [Python](patterns/dynamic_programming/subset_sum.py) | — |
| target sum | [Python](patterns/dynamic_programming/target_sum.py) | — |
| unbounded knapsack | [Python](patterns/dynamic_programming/unbounded_knapsack.py) | — |
| word break | [Python](patterns/dynamic_programming/word_break.py) | [recursion](patterns/recursion/) |
| zero one knapsack problem | [Python](patterns/dynamic_programming/zero_one_knapsack_problem.py) | — |

</details>

<details>
<summary>bit manipulation (14 files)</summary>

| Problem / exercise | Solutions | Secondary patterns |
| --- | --- | --- |
| clear bits in range | [Python](patterns/bit_manipulation/clear_bits_in_range.py) | — |
| clear ith bit | [Python](patterns/bit_manipulation/clear_ith_bit.py) | — |
| clear last i bits | [Python](patterns/bit_manipulation/clear_last_i_bits.py) | — |
| convert to binary | [Python](patterns/bit_manipulation/convert_to_binary.py) | — |
| count bits | [Python](patterns/bit_manipulation/count_bits.py) | — |
| fast exponentiation | [Python](patterns/bit_manipulation/fast_exponentiation.py) | — |
| find two non repeating elements | [Python](patterns/bit_manipulation/find_two_non_repeating_elements.py) | — |
| finding duplicates bitwise | [C++](patterns/bit_manipulation/finding_duplicates_bitwise.cpp) | — |
| get ith bit | [Python](patterns/bit_manipulation/get_ith_bit.py) | — |
| power of two | [Python](patterns/bit_manipulation/power_of_two.py) | — |
| replace bits | [Python](patterns/bit_manipulation/replace_bits.py) | — |
| set ith bit | [Python](patterns/bit_manipulation/set_ith_bit.py) | — |
| sets bits in binary | [Python](patterns/bit_manipulation/sets_bits_in_binary.py) | — |
| update ith bit | [Python](patterns/bit_manipulation/update_ith_bit.py) | — |

</details>

<details>
<summary>math and number theory (28 files)</summary>

| Problem / exercise | Solutions | Secondary patterns |
| --- | --- | --- |
| combination formula pascal triangle | [C++](patterns/math_and_number_theory/combination_formula_pascal_triangle.cpp) | — |
| days between dates | [Python](patterns/math_and_number_theory/days_between_dates.py) | — |
| encryption algorithms | [Notebook](patterns/math_and_number_theory/encryption_algorithms.ipynb) | — |
| euclids gcd lcm | [Python](patterns/math_and_number_theory/euclids_gcd_lcm.py) | — |
| factorial large number | [C++](patterns/math_and_number_theory/factorial_large_number.cpp) | — |
| fast power calculation | [C++](patterns/math_and_number_theory/fast_power_calculation.cpp) | — |
| find gcd | [C++](patterns/math_and_number_theory/find_gcd.cpp) | — |
| gcd hcf lcm | [Python](patterns/math_and_number_theory/gcd_hcf_lcm.py) | — |
| karatsuba | [Python](patterns/math_and_number_theory/karatsuba.py) | — |
| larousse | [Python](patterns/math_and_number_theory/larousse.py) | — |
| leap year | [Java](patterns/math_and_number_theory/leap_year.java) | — |
| missing number | [C++](patterns/math_and_number_theory/missing_number.cpp) | — |
| missing number in array | [C++](patterns/math_and_number_theory/missing_number_in_array.cpp) | — |
| monte carlo daily coding | [Python](patterns/math_and_number_theory/monte_carlo_daily_coding.py) | — |
| palindrome | [C++](patterns/math_and_number_theory/palindrome.cpp) | — |
| pascal triangle | [Python](patterns/math_and_number_theory/pascal_triangle.py) | — |
| pascals triangle | [Python](patterns/math_and_number_theory/pascals_triangle.py) | — |
| prime number | [C++](patterns/math_and_number_theory/prime_number.cpp) | — |
| prime number1 | [Java](patterns/math_and_number_theory/prime_number1.java) | — |
| prime sieve | [Python](patterns/math_and_number_theory/prime_sieve.py) | — |
| prime sieve prime numbers | [Python](patterns/math_and_number_theory/prime_sieve_prime_numbers.py) | — |
| prime visits | [Python](patterns/math_and_number_theory/prime_visits.py) | — |
| random element from stream daily coding | [Python](patterns/math_and_number_theory/random_element_from_stream_daily_coding.py) | — |
| repeat and missing | [Python](patterns/math_and_number_theory/repeat_and_missing.py) | — |
| reverse integer | [Java](patterns/math_and_number_theory/reverse_integer.java) | — |
| strassen | [Python](patterns/math_and_number_theory/strassen.py) | — |
| sum of all submatrices | [C++](patterns/math_and_number_theory/sum_of_all_submatrices.cpp) | — |
| trailing zeroes | [Python](patterns/math_and_number_theory/trailing_zeroes.py) | — |

</details>
