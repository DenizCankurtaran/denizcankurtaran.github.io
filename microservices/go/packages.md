# Packages

Each source file beginns with a package declaration.
Main package is special, contains not a library, but a standalone executable.
In main package a main function is needed.

Programm will not compile if there are missing import or *unnecessary ones* ones.


# Import / Package Workflow

## GOPATH
$GOPATH => Points to all projects

GOPATH=~/folder/go/projects/

## Init project
Example: if my project is on Gitlab and the Gitlab project name is called HelloWorld then my command should look like this:
```
go mod init gitlab.beuth-hochschule.de/microservice-entwicklung/HelloWorld 
```

## Example project
Example project located at ~/folder/go/projects/HelloWorld/

## file structure
```
HelloWorld/
 - main.go
 - TestPackage/
   - test.go
```

main.go
```
package main
import (
  "fmt"
  "gitlab.beuth-hochschule.de/microservice-entwicklung/HelloWorld/TestPackage"
)

func main() {
  fmt.Println(test.HelloWorld)
}
```

TestPackage/test.go
```
package TestPackage

var HelloWorld = "Hello World"

```
