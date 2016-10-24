train <- read.csv("C:/Users/alexis/Desktop/Cornell_2016-2017/learning_with_big_data/project/midreport.csv", sep=";")
attach(train)

train <- read.csv("C:/Users/alexis/Desktop/Cornell_2016-2017/learning_with_big_data/project/train.csv", sep=";")
attach(train)
trainbis<-train[amount_tsh>0 & amount_tsh<1050 & longitude!=0 & latitude!=0,]
trainter<-trainbis[c(1:800),]
########################### regions
library('plyr')
cc=count(train,'region')

list_region=levels(region)
mean_functional_region=rep(0,nrow(cc))
for (i in 1:nrow(cc)){
  mean_functional_region[i]<-mean(train$X1.0[region==list_region[i]])
  
}

cc["proportion_bad"]<-mean_functional_region

library(plotly)
plot_ly(cc, x = cc$region, y = cc$proportion_bad,type="bar")
plot_ly(trainbis,x=trainbis$gps_height,type="histogram")
############################


x<-list(title=trainbis$gps_height[c(1:300)])
plot_ly(x=as.character(trainbis[c(1:300),"gps_height"]),color=as.character(trainbis[c(1:300),"X1.0"]),type="box") %>% layout(title="boites-moustaches pour 0 et 1",xaxis=x) #"boite a moustaches"

#x<-list(title=trainbis$gps_height)
#plot_ly(x=as.character(trainbis[,"gps_height"]),color=as.character(trainbis[,"status_group"]),type="box") %>% layout(title="boites-moustaches pour 0 et 1",xaxis=x) #"boite a moustaches"

x<-list(title=input$var1)
y<-list(title=input$var2)
p<-plot_ly(data = trainbis,x=trainbis[,"latitude"],y=trainbis[,"longitude"],mode="markers",color=trainbis[,"X1.0"])
p<-layout(p,title="where are the working wells ?",xaxis=x,yaxis=y,shapes=list(
  list(type="rect",fillcolor="blue",line=list(color="black"),opacity=0.2,x0=max(fctprim()$box[[input$num_box]][1,input$var1],min(x(),na.rm=T)),x1=min(max(x(),na.rm=T),fctprim()$box[[input$num_box]][2,input$var1]),xref="3",y0=max(min(y(),na.rm=T),fctprim()$box[[input$num_box]][1,input$var2]),y1=min(max(y(),na.rm=T),fctprim()$box[[input$num_box]][2,input$var2]),yref="1")))

library(ggplot2)

dat1 = data.frame(x=trainbis[status_group=="functional","amount_tsh"], group="functional")
dat2 = data.frame(x=trainbis[status_group=="non functional","amount_tsh"], group="non functional")
dat = rbind(dat1, dat2)

ggplot(dat, aes(x, fill=group, colour=group)) +
  geom_histogram(breaks=seq(0,1000,5), alpha=0.6, 
                 position="identity", lwd=0.2)+ggtitle("count vs amount_tsh")

write.csv(trainter,file="project_longitude_nonnulle_800rows.csv")


#Shiny app

#boxplot
output$e_boite<-renderPlotly({
  x<-list(title=input$var)
  plot_ly(x=data()[,input$var],color=as.character(data()[,input$reponse]),type="box") %>% layout(title="boites-moustaches pour 0 et 1",xaxis=x)
})


#plotting the blue box
output$g<-renderPlotly({
  x<-list(title=input$var1)
  y<-list(title=input$var2)
  p<-plot_ly(data = data(),x=x(),y=y(),mode="markers",color=z())
  p<-layout(p,title="correlations between variables",xaxis=x,yaxis=y,shapes=list(
    list(type="rect",fillcolor="blue",line=list(color="black"),opacity=0.2,x0=max(fctprim()$box[[input$num_box]][1,input$var1],min(x(),na.rm=T)),x1=min(max(x(),na.rm=T),fctprim()$box[[input$num_box]][2,input$var1]),xref="3",y0=max(min(y(),na.rm=T),fctprim()$box[[input$num_box]][1,input$var2]),y1=min(max(y(),na.rm=T),fctprim()$box[[input$num_box]][2,input$var2]),yref="1")))
  p
})