/** @odoo-module */

import { registry } from '@web/core/registry';
const {Component,useState,onWillStart,onMounted}= owl;
import { KpiCard } from "./kpi_card/kpi_card"
import { ChartRenderer } from "./chart_renderer/chart_renderer"
import { loadJS } from "@web/core/assets"
import { useService } from "@web/core/utils/hooks"
import {getColor} from "@web/views/graph/colors"
import Dialog from 'web.Dialog';
import core from 'web.core';
var _t = core._t;
 export class TodoDashbordc extends Component{

 async getTopsend(){

let domain =[['progress' ,'in',['send']]]
  if (this.state.period == 1){
            domain.push(['Departmet_ids','=', 'AIS'])
        }else if(this.state.period == 2){
            domain.push(['Departmet_ids','=', 'FLIR'])
            }else if(this.state.period == 3){
            domain.push(['Departmet_ids','=', 'SAGEM'])
  }else if(this.state.period == 4){
            domain.push(['Departmet_ids','=', 'CCTV'])
  }
 const data = await this.orm.searchCount("workshop.sendreceived",domain)
 const data2 = await this.orm.readGroup("workshop.sendreceived",domain,['REGION','QTY'],['REGION'])

  this.state.Topsend = {
     data: {

     labels: data2.map(d =>d.REGION) ,

              datasets: [
              {
                label: data2.map(d =>d.REGION) ,
                data: data2.map(d =>d.QTY),
                hoverOffset: 5,
                backgroundColor:data2.map((_,index) => getColor(index)),
              }]
          }
     }
}
async getTopDone(){

 let domain =[['progress' ,'in',['done']]]
  if (this.state.period == 1){
            domain.push(['Departmet_ids','=', 'AIS'])
        }else if(this.state.period == 2){
            domain.push(['Departmet_ids','=', 'FLIR'])
            }else if(this.state.period == 3){
            domain.push(['Departmet_ids','=', 'SAGEM'])
  }else if(this.state.period == 4){
            domain.push(['Departmet_ids','=', 'CCTV'])
  }
const data2 = await this.orm.readGroup("workshop.sendreceived",domain,['REGION','QTY'],['REGION'])

  this.state.TopDone = {
     data: {

     labels: data2.map(d =>d.REGION) ,

              datasets: [
              {
                label: data2.map(d =>d.REGION) ,
                data: data2.map(d =>d.QTY),
                hoverOffset: 5,
                backgroundColor:data2.map((_,index) => getColor(index)),
              }]
          }

     }
}



    setup(){
        this.state = useState({
        period:0,
                number_send_value: {
                value:20,
                percentage:5,
            },
                    number_done_value: {
                value:20,
                percentage:70,
            },
                    number_projection_value: {
                value:20,
                percentage:20,
            },
                  number_Replacement_value: {
                value:20,
                percentage:7,
            }
        })
             this.orm = useService("orm")
               this.actionService = useService("action")


            onWillStart(async ()=>{

            await this.number_send()
            await this.number_done()
            await this.number_projection()
            await this.number_Replacement()
           await  this. getTopsend()
           await this.getTopDone()

        })
    }

     async onChangePeriod(){

            await this.number_send()
            await this.number_done()
            await this.number_projection()
            await this.number_Replacement()
            await  this. getTopsend()
            await this.getTopDone()
    }


async number_send(){
let domain =[['progress' ,'in',['send']]]
  if (this.state.period == 1){
            domain.push(['Departmet_ids','=', 'AIS'])
        }else if(this.state.period == 2){
            domain.push(['Departmet_ids','=', 'FLIR'])
            }else if(this.state.period == 3){
            domain.push(['Departmet_ids','=', 'SAGEM'])
  }else if(this.state.period == 4){
            domain.push(['Departmet_ids','=', 'CCTV'])
  }
 const data = await this.orm.searchCount("workshop.sendreceived",domain)
 this.state.number_send_value.value = data



}
async number_done(){
let domain =[['progress' ,'in',['done']]]
  if (this.state.period == 1){
            domain.push(['Departmet_ids','=', 'AIS'])
        }else if(this.state.period == 2){
            domain.push(['Departmet_ids','=', 'FLIR'])
            }else if(this.state.period == 3){
            domain.push(['Departmet_ids','=', 'SAGEM'])
  }else if(this.state.period == 4){
            domain.push(['Departmet_ids','=', 'CCTV'])
  }
 const data = await this.orm.searchCount("workshop.sendreceived",domain)
 this.state.number_done_value.value = data

}
async number_projection(){
let domain =[['progress' ,'in',['IN']]]
  if (this.state.period == 1){
            domain.push(['Departmet_ids','=', 'AIS'])
        }else if(this.state.period == 2){
            domain.push(['Departmet_ids','=', 'FLIR'])
            }else if(this.state.period == 3){
            domain.push(['Departmet_ids','=', 'SAGEM'])
  }else if(this.state.period == 4){
            domain.push(['Departmet_ids','=', 'CCTV'])
  }
 const data = await this.orm.searchCount("workshop.sendreceived",domain)
 this.state.number_projection_value.value = data

}
async number_Replacement(){
let domain =[['progress' ,'in',['new']]]
  if (this.state.period == 1){
            domain.push(['Departmet_ids','=', 'AIS'])
        }else if(this.state.period == 2){
            domain.push(['Departmet_ids','=', 'FLIR'])
            }else if(this.state.period == 3){
            domain.push(['Departmet_ids','=', 'SAGEM'])
  }else if(this.state.period == 4){
            domain.push(['Departmet_ids','=', 'CCTV'])
  }
 const data = await this.orm.searchCount("workshop.sendreceived",domain)
 this.state.number_Replacement_value.value = data

}
  async viewQuotations(){
        this.actionService.doAction("AIS_WORKSHOP.action_WorkShop_sendreceived")
    }

}

TodoDashbordc.template = 'AIS_WORKSHOP.TodoDashbord'
TodoDashbordc.components = { KpiCard ,  ChartRenderer}
registry.category("actions").add('AIS_WORKSHOP.action_todo_dash', TodoDashbordc);


