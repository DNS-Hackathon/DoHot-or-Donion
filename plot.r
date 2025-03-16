#!/usr/bin/env Rscript
library(ggplot2)

measure <- read.csv('measurements.csv')
measure$protocol_variant <- ifelse(measure$variant=="", measure$protocol, paste(measure$protocol, measure$variant, sep="-"))
quit()
measure$dig_begin <- as.POSIXct(measure$dig_begin)
measure$dig_end <- as.POSIXct(measure$dig_end)
measure$dig_duration <- as.numeric(measure$dig_end - measure$dig_begin, units="secs")
measure$ok <- measure$dig_out != ""

p <- ggplot(measure) +
  aes(x=protocol_variant, y=dig_duration, color=ok) +
  coord_flip() +
  labs(title="Variants of anonymous DNS lookup") +
  scale_x_discrete("DNS lookup protocol variant") +
  scale_y_continuous("Time of dig execution") +
  geom_point(alpha=0.2)

ggsave("/tmp/p1.pdf")
