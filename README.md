# trac-javadoc
This macro takes the javadoc that is specified above a class or interface and embeds that as text in the wiki.
It will search all of the repositories configured in trac for a file with the specified path and use the first one that is found.

## Usage
```markdown
[[JavaDoc(trunk/com/foo/Bar.java)]]
```
with a file in the repository named in the path trunk/com/foo/Bar.java 
```java
package com.foo;

/**
 This is a sample comment
**/
public class Bar {
	public void baz();
}
```
will output a link to Bar.java in the repository with the text "This is a sample comment" under it in a code block.

## Installation
TODO

