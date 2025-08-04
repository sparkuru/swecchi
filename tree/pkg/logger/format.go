package logger

import (
	"fmt"
	"time"
)

type LogEntry struct {
	Time    time.Time
	Level   LogLevel
	Message string
	File    string
	Line    int
	Prefix  string
}

type Formatter interface {
	Format(entry LogEntry) string
}

type DefaultFormatter struct{}

func (f *DefaultFormatter) Format(entry LogEntry) string {
	return fmt.Sprintf("%s %s [%s] %s:%d - %s\n",
		entry.Time.Format("2006-01-02 15:04:05"),
		entry.Prefix,
		entry.Level.String(),
		entry.File,
		entry.Line,
		entry.Message,
	)
}

type ColorFormatter struct{}

const (
	ColorReset  = "\033[0m"
	ColorRed    = "\033[31m"
	ColorYellow = "\033[33m"
	ColorBlue   = "\033[34m"
	ColorPurple = "\033[35m"
	ColorCyan   = "\033[36m"
	ColorGray   = "\033[37m"
	ColorWhite  = "\033[97m"
)

func (f *ColorFormatter) getColor(level LogLevel) string {
	switch level {
	case DEBUG:
		return ColorGray
	case INFO:
		return ColorCyan
	case WARN:
		return ColorYellow
	case ERROR:
		return ColorRed
	case FATAL:
		return ColorPurple
	default:
		return ColorWhite
	}
}

func (f *ColorFormatter) Format(entry LogEntry) string {
	color := f.getColor(entry.Level)
	return fmt.Sprintf("%s%s %s [%s] %s:%d - %s%s\n",
		color,
		entry.Time.Format("2006-01-02 15:04:05"),
		entry.Prefix,
		entry.Level.String(),
		entry.File,
		entry.Line,
		entry.Message,
		ColorReset,
	)
}

type JSONFormatter struct{}

func (f *JSONFormatter) Format(entry LogEntry) string {
	return fmt.Sprintf(`{"time":"%s","level":"%s","file":"%s","line":%d,"message":"%s"}`+"\n",
		entry.Time.Format(time.RFC3339),
		entry.Level.String(),
		entry.File,
		entry.Line,
		entry.Message,
	)
}

type SimpleFormatter struct{}

func (f *SimpleFormatter) Format(entry LogEntry) string {
	return fmt.Sprintf("[%s] %s\n",
		entry.Level.String(),
		entry.Message,
	)
}
