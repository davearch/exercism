// Package space gives a type for planets and an Age method.
package space

// Planet is custom type for planets.
type Planet string

// earthYearInSeconds is the number of seconds in an Earth year.
const earthYearInSeconds float64 = 31557600

// Age returns the age a person would be for the given planet.
func Age(seconds float64, planet Planet) float64 {
	planets := map[Planet]float64{
		"Earth":   1,
		"Mercury": 0.2408467,
		"Venus":   0.61519726,
		"Mars":    1.8808158,
		"Jupiter": 11.862615,
		"Saturn":  29.447498,
		"Uranus":  84.016846,
		"Neptune": 164.79132,
	}
	return seconds / (earthYearInSeconds * planets[planet])
}
