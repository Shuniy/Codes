"""
HTTPRouter using a Trie
For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure we learned previously.

There are many different implementations of HTTP Routers such as regular expressions or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a handler.

First we need to implement a slightly different Trie than the one we used for autocomplete. Instead of simple words the Trie will contain a part of the http path at each node, building from the root node /

In addition to a path though, we need to know which function will handle the http request. In a real router we would probably pass an instance of a class like Python's SimpleHTTPRequestHandler which would be responsible for handling requests to that path. For the sake of simplicity we will just use a string that we can print out to ensure we got the right handler

We could split the path into letters similar to how we did the autocomplete Trie, but this would result in a Trie with a very large number of nodes and lengthy traversals if we have a lot of pages on our site. A more sensible way to split things would be on the parts of the path that are separated by slashes ("/"). A Trie with a single path entry of: "/about/me" would look like:

(root, None) -> ("about", None) -> ("me", "About Me handler")

We can also simplify our RouteTrie a bit by excluding the suffixes method and the endOfWord property on RouteTrieNodes. We really just need to insert and find nodes, and if a RouteTrieNode is not a leaf node, it won't have a handler which is fine.

Next we need to implement the actual Router. The router will initialize itself with a RouteTrie for holding routes and associated handlers. It should also support adding a handler by path and looking up a handler by path. All of these operations will be delegated to the RouteTrie.

Hint: the RouteTrie stores handlers under path parts, so remember to split your path around the '/' character

Bonus Points: Add a not found handler to your Router which is returned whenever a path is not found in the Trie.

More Bonus Points: Handle trailing slashes! A request for '/about' or '/about/' are probably looking for the same page. Requests for '' or '/' are probably looking for the root handler. Handle these edge cases in your Router.

It is similar to problem 5, except for the edge cases, like "root handler", and working with a hierarchy of web pages instead of strings. This problem is focused on the development of the of a trie a data structure derived from a tree, suited for a good ratio between time and space complexity.

Time and Space complexity
For the trie, time complexity of searching and inserting from a trie depends on the length of the path n that’s being searched for, inserted, making the runtime of these operations O(n). Looking into the space complexity of a trie, the worst case, would be when we have a path (or paths), with no common folders between them, hence having, a node for each path block (path between forward slashes). Resulting in a space complexity of
O(n).
"""
class RouteTrieNode(object):
    """  A RouteTrieNode will be similar to our autocomplete TrieNode...
    with one additional element, a handler. """

    def __init__(self):
        """ Initialize the node with children as before, plus a handler """
        self.children = {}
        self.handler = None

    def insert(self, path_block):
        """ Insert the node as before """
        if path_block not in self.children:
            self.children[path_block] = RouteTrieNode()
        else:
            pass

class RouteTrie(object):
    """ A RouteTrie will store our routes and their associated handlers """

    def __init__(self, root_handler):
        self.root = RouteTrieNode()
        self.handler = root_handler

    def insert(self, path, handler):
        """ Similar to our previous example you will want to recursively add nodes
        Make sure you assign the handler to only the leaf (deepest) node of this path """
        node = self.root

        for path_block in path:
            node.insert(path_block)
            node = node.children[path_block]

        node.handler = handler

    def find(self, path):
        """ Starting at the root, navigate the Trie to find a match for this path
        Return the handler for a match, or None for no match """

        node = self.root

        for path_block in path:
            if path_block not in node.children:
                return None
            node = node.children[path_block]

        return node.handler

class Router:
    """ The Router class will wrap the Trie and handle """
    def __init__(self, root_handler, non_found_handler):
        """ Create a new RouteTrie for holding our routes
        You could also add a handler for 404 page not found responses as well"""
        self.router = RouteTrie(root_handler=root_handler)
        self.non_found_handler = non_found_handler

    def add_handler(self, raw_path, handler):
        """
            Add a handler for a path
            You will need to split the path and pass the pass parts
            as a list to the RouteTrie
        """
        path = self._split_path(raw_path)
        self.router.insert(path, handler)

    def lookup(self, raw_path):
        """
            lookup path (by parts) and return the associated handler
        you can return None if it's not found or
        return the "not found" handler if you added one
        bonus points if a path works with and without a trailing slash
        e.g. /about and /about/ both return the /about handler
        """
        path = self._split_path(raw_path)

        if len(path) == 0:
            return self.router.handler

        finding = self.router.find(path)

        if finding = self.router.find(path)

        if finding is None:
            return self.non_found_handler

        else:
            return finding

    @staticmethod
    def _split_path(raw_path):
        """
        you need to split the path into parts for
        both the add_handler and loopup functions,
        so it should be placed in a function here
        """
        result_temp = raw_path.split(sep = '/')
        return [element for element in result_temp if element != '']

# Here are some test cases and expected outputs you can use to test your implementation
# create the router and add a route
# remove the 'not found handler' if you did not implement this
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
# root handler
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home"))
# not found handler
print(router.lookup("/home/about"))  # should print 'about handler'
# about handler
# should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/"))
# about handler
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me"))
# not found handler
