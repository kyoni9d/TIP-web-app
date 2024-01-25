package main

import (
	"net/http"

	"github.com/brianvoe/gofakeit/v6"
	"github.com/gin-gonic/gin"
)

func ExampleHandler(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{"email": gofakeit.Email()})
}

func main() {
	router := gin.Default()
	router.GET("/", ExampleHandler)
	router.Run()
}
