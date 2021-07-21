from flask import Flask, request,send_file
import numpy as np
import math
#import pandas as pd
import matplotlib.pyplot as plt, mpld3


app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        operation = request.form['operation']
        unit1 = request.form['unit1']
        unit2 = request.form['unit2']
        unit3 = request.form['unit3']
        try:
            number1 = float(request.form["number1"])
            mword=''
        except:
            number1=1
            mword='Default value of mass taken is 1 kg as input was not a number'
            unit1 = '11'
        try:
            number2 = float(request.form["number2"])
            kword=''
        except:
            number2 =1
            kword='Default value of Stiffness taken is 1 N/m as input was not a number'
            unit2 = '21'
        try:
            number3 = float(request.form["number3"])
            dword=''
        except:
            number3 = 0.1
            dword='Default value of Damping ratio taken is 0.1 as input was not a number'
        try:
            number4 = float(request.form["number4"])
            fword=''
        except:
            number4 = 0
            fword='Default value of Harmonic input frequency taken is 0 as input was not a number'

        m = number1
        k = number2
        dpratio=number3
        freq = number4
        freqq = freq
        if operation == "+":
            if unit1 == '11':
                m1 = m
            elif unit1 == '12':
                m1 = m/1000
            else:
                m1 = m/2.20462
            if unit2 == '21':
                k1 = k
            elif unit2 == '22':
                k1 = 1000*k
            else:
                k1 = k*100*4.44822/2.54
            wn = np.power((k1/m1),0.5)
            fn = 1/(2*math.pi)*wn
            T = 1/fn
            cc = 2*m1*wn
            c = cc*dpratio
            wd = wn*np.power((1-(dpratio*dpratio)),0.5)
            fd = 1/(2*math.pi)*wd
            if dpratio == 0:
                q = 'Infinity'
            else:
                q = 1/(2*dpratio)
            if unit1 == '11':
                unit1 = 'kg'
            elif unit1 == '12':
                unit1= 'gram'
            else:
                unit1 = 'lb'
            if unit2 == '21':
                unit2 = 'N/m'
            elif unit2 == '22':
                unit2 = 'N/mm'
            else:
                unit2 = 'lbf/in'
            try:
                result=(round(wn,2),round(fn,2),round(T,2),round(cc,2),round(c,2),round(wd,2),round(fd,2),round(q,2),round(m,2),round(k,2),dpratio,round(freq,2),unit1,unit2,mword,kword,dword,fword)
            except:
                result=(round(wn,2),round(fn,2),round(T,2),round(cc,2),round(c,2),round(wd,2),round(fd,2),q,round(m,2),round(k,2),dpratio,round(freq,2),unit1,unit2,mword,kword,dword,fword)
            return '''
                <html>
                        <body style="background-color:powderblue;">
                    <h1 style="text-align:center;color:brown;background-color:yellow;"> SINGLE DEGREE OF FREEDOM SYSTEMS (SDOF)</p></h1>
                    <h1 style="text-align:center;color:brown;background-color:yellow">- VIBRATION CALCULATOR</p></h1>
                    <br/>

                        <h3 style="background-color:#99bfff">INPUT PARAMETERS:</h3>

                        <p>{result[14]}</p>
                        <p>{result[15]}</p>
                        <p>{result[16]}</p>
                        <p>{result[17]}</p>
                        <table style="width:30%">
                        <tr>
                        <th>Parameter</th>
                        <th>Value</th>
                        <th>Unit</th>
                        </tr>
                        <tr>
                        <td>Mass [m]</td>
                        <td>{result[8]}</td>
                        <td>{result[12]}</td>
                        </tr>
                        <tr>
                        <td>Spring rate (Stiffness) [k]</td>
                        <td>{result[9]}</td>
                        <td>{result[13]}</td>
                        </tr>
                        <tr>
                        <td>Damping ratio (coefficient) [ζ]</td>
                        <td>{result[10]}</td>
                        <td>--</td>
                        </tr>
                        <tr>
                        <td>Harmonic input frequency [Ω]</td>
                        <td>0</td>
                        <td>Hz</td>
                        </tr>
                        </table>
                        </br>

                        <h3 style="background-color:#99bfff">RESULTS:</h3>
                        <table style="width:40%">
                        <tr>
                        <th><h4>Parameter</h4></th>
                        <th><h4>Value</h4></th>
                        <th><h4>Unit</h4></th>
                        </tr>
                        <tr>
                        <td><p style="color:red">Cicular frequency [wn]</p></td>
                        <td>{result[0]} </td>
                        <td>rad/s</td>
                        </tr>
                        <tr>
                        <td><p style="color:red">Natural frequency [fn]</p></td>
                        <td>{result[1]} </td>
                        <td>Hz</td>
                        </tr>
                        <tr>
                        <td><p style="color:red">Period of oscilattion [T] </p></td>
                        <td>{result[2]}</td>
                        <td>s</td>
                        </tr>
                        <tr>
                        <td><p style="color:red">Critical damping [cc]</p></td>
                        <td>{result[3]}</td>
                        <td>Ns/m</td>
                        </tr>
                        <tr>
                        <td><p style="color:red">Damping factor [c]</p></td>
                        <td>{result[4]}</td>
                        <td>Ns/m</td>
                        </tr>
                        <tr>
                        <td><p style="color:red">Damped natural angular frequency [wd] </p></td>
                        <td>{result[5]}</td>
                        <td>rad/s</td>
                        </tr>
                        <tr>
                        <td><p style="color:red">Damped natural frequency [fd]</p></td>
                        <td> {result[6]}</td>
                        <td>Hz</td>
                        </tr>
                        <tr>
                        <td><p style="color:red">Quality factor [Q] </p></td>
                        <td>{result[7]}</td>
                        <td>--</td>
                        </tr>
                        <td><p style="color:red">Transmissibility [TR]</p></td>
                        <td>--</td>
                        <td>--</td>
                        </tr>

                        </table>
                        <p><a href="/">Click here to calculate again</a>
                        </br>
                        </br>
                        <br/>
                                      <p><h2>Definitions:</h2><br/>
                                      <b>Critical damping:</b> The minimum amount of viscous damping that results in a displaced system returning to its original position without oscillation. <br/>
                                       </br>
                                       <b>Damped natural frequency:</b> In the presence of damping, the frequency at which the system vibrates when disturbed. Damped natural frequency is less than undamped natural frequency.<br/>
                                       </br>
                                       <b>Damping ratio:</b> The ratio of actual damping to critical damping. It is a dimensionless measure describing how oscillations in a system decay after a disturbance.<br/>
                                       </br>
                                       <b>Forced vibrations:</b> Oscillations about a system's equilibrium position in the presence of an external excitation.<br/>
                                       </br>
                                       <b>Free  vibrations:</b> Oscillations about a system's equilibrium position in the absence of an external excitation.<br/>
                                       </br>
                                       <b>Natural frequency:</b> The frequency at which a system vibrates when set in free vibration.<br/>
                                       </br>
                                       <b>Undamped natural frequency:</b> In the absence of damping, the frequency at which the system vibrates when disturbed.<br/>
                                       </br>
                                       <b>Period of Oscillation:</b> The time in seconds required for one cycle.<br/>
                                       </br>
                                       <b>Transmissiblity:</b> The ratio of output amplitude to input amplitude at same frequency. Following 2 conditions have same transmissiblity value.<br/>
                                       <p>-- Transmissiblity between harmonic motion excitation from the base (input) and motion response of mass (output) Ex: Car runing on the road. Car body is m, base motion excitation is road disturbances.</p>
                                       <p style="text-align:center"><img src="https://amesweb.info/Vibration/images/SDOF_BaseDriven.jpg" alt="Italian Trulli"></p>
                                       <p>-- Harmonic forcing excitation to mass (Input) and force transmitted to base (output). Ex: A rotating machine generating force during operation and transmitting to its base.</p>
                                       <p style="text-align:center"><img src=https://amesweb.info/Vibration/images/SDOF_MassDriven.jpg></p>
                                       <br>
                                       <b>Quality Factor:</b> Transmissibility at resonance, which is the system’s highest possible response ratio.<br/>
                                      </br>
                                        <br/>
                                        <h3>Single Degree of Freedom Vibration Equations:</h3>
                                        <a data-flickr-embed="true" href="https://www.flickr.com/photos/192618941@N08/51054280162/in/dateposted/" title="Capture"><img src="https://live.staticflickr.com/65535/51054280162_92a7700327_b.jpg" width="700" height="500" alt="Capture"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>
                                        </br>
                                        </br>

                        </br>
                        </br>
                        <p><a href="/">Click here to calculate again</a>
                        </br>
                    </body>
                </html>

                '''.format(result=result)

        elif operation == "-":
            if unit1 == '11':
                m1 = m
            elif unit1 == '12':
                m1 = m/1000
            else:
                m1 = m/2.20462
            if unit2 == '21':
                k1 = k
            elif unit2 == '22':
                k1 = 1000*k
            else:
                k1 = k*100*4.44822/2.54
            freq=freq*2*math.pi
            wn = np.power((k1/m1),0.5)
            fn = 1/(2*math.pi)*wn
            T = 1/fn
            cc = 2*m1*wn
            c = cc*dpratio
            wd = wn*np.power((1-(dpratio*dpratio)),0.5)
            fd = 1/(2*math.pi)*wd
            if dpratio == 0:
                q = 'Infinity'
            else:
                q = 1/(2*dpratio)
            a = 1+(np.power(2*dpratio*freq/wn,2))
            b = np.power((1-(np.power((freq/wn),2))),2)
            c1 = np.power(2*dpratio*freq/wn,2)
            tr = np.power(a/(b+c1),0.5)
            freq1=[]
            tr1=[]
            freq3 = 0
            #freqratio = int(freq/fn)
            for i in range(1,10000000):
                freqratio=freq3/wn
                if freqratio >= 0.099:
                    freq1.append(freqratio)
                a = 1+(np.power(2*dpratio*freq3/wn,2))
                b = np.power((1-(np.power((freq3/wn),2))),2)
                c1 = np.power(2*dpratio*freq3/wn,2)
                tr2 = np.power(a/(b+c1),0.5)
                if freqratio >= 0.099:
                    tr1.append(tr2)
                freq3 = 0.01+freq3
                if int(freqratio) >= 3:
                    break
            fig, ax = plt.subplots()
            ax.loglog(freq1, tr1,c='r')
            plt.grid()
            #ax.loglog(freq,tr,'+')
            plt.title('Transmissiblity vs Frequency Ratio Graph(log-log)')
            plt.xlabel('Frequency Ratio')
            plt.ylabel('Transmissiblity [TR]')
            html_text = mpld3.fig_to_html(fig)
            if unit1 == '11':
                unit1 = 'kg'
            elif unit1 == '12':
                unit1= 'gram'
            else:
                unit1 = 'lb'
            if unit2 == '21':
                unit2 = 'N/m'
            elif unit2 == '22':
                unit2 = 'N/mm'
            else:
                unit2 = 'lbf/in'
            try:
                result=(round(wn,2),round(fn,2),round(T,2),round(cc,2),round(c,2),round(wd,2),round(fd,2),round(q,2),round(tr,2),html_text,round(m,2),round(k,2),dpratio,round(freqq,2),unit1,unit2,mword,kword,dword,fword)
            except:
                result=(round(wn,2),round(fn,2),round(T,2),round(cc,2),round(c,2),round(wd,2),round(fd,2),q,round(tr,2),html_text,round(m,2),round(k,2),dpratio,round(freqq,2),unit1,unit2,mword,kword,dword,fword)

            return '''
                    <html>
                        <body>
                    <body style="background-color:powderblue;">
                <h1 style="text-align:center;color:brown;background-color:yellow;"> SINGLE DEGREE OF FREEDOM SYSTEMS (SDOF)</p></h1>
                <h1 style="text-align:center;color:brown;background-color:yellow">- VIBRATION CALCULATOR</p></h1>
                <br/>
                <p>{result[16]}</p>
                <p>{result[17]}</p>
                <p>{result[18]}</p>
                <p>{result[19]}</p>

                <h3 style="background-color:#99bfff">INPUT PARAMETERS:</h3>
                        <table style="width:30%">
                        <tr>
                        <th><h4>Parameter</h4></th>
                        <th><h4>Value</h4></th>
                        <th><h4>Unit</h4></th>
                        </tr>
                        <tr>
                        <td>Mass [m]</td>
                        <td>{result[10]}</td>
                        <td>{result[14]}</td>
                        </tr>
                        <tr>
                        <td>Spring rate (Stiffness) [k]</td>
                        <td>{result[11]}</td>
                        <td>{result[15]}</td>
                        </tr>
                        <tr>
                        <td>Damping raito (coefficient) [ζ]</td>
                        <td>{result[12]}</td>
                        <td>--</td>
                        </tr>
                        <tr>
                        <td>Harmonic input frequency [Ω]</td>
                        <td>{result[13]}</td>
                        <td>Hz</td>
                        </tr>
                        </table>

                        <h3 style="background-color:#99bfff">RESULTS:</h3>

                        <table style="width:40%">
                        <tr>
                        <th><h4>Parameter</h4></th>
                        <th><h4>Value</h4></th>
                        <th><h4>Unit</h4></th>
                        </tr>
                        <tr>
                        <td><p style="color:red">Cicular frequency [wn]</p></td>
                        <td>{result[0]} </td>
                        <td>rad/s</td>
                        </tr>
                        <tr>
                        <td><p style="color:red">Natural frequency [fn]</p></td>
                        <td>{result[1]} </td>
                        <td>Hz</td>
                        </tr>
                        <tr>
                        <td><p style="color:red">Period of oscilattion [T] </p></td>
                        <td>{result[2]}</td>
                        <td>s</td>
                        </tr>
                        <tr>
                        <td><p style="color:red">Critical damping [cc]</p></td>
                        <td>{result[3]}</td>
                        <td>Ns/m</td>
                        </tr>
                        <tr>
                        <td><p style="color:red">Damping factor [c]</p></td>
                        <td>{result[4]}</td>
                        <td>Ns/m</td>
                        </tr>
                        <tr>
                        <td><p style="color:red">Damped natural angular frequency [wd] </p></td>
                        <td>{result[5]}</td>
                        <td>rad/s</td>
                        </tr>
                        <tr>
                        <td><p style="color:red">Damped natural frequency [fd]</p></td>
                        <td> {result[6]}</td>
                        <td>Hz</td>
                        </tr>
                        <tr>
                        <td><p style="color:red">Quality factor [Q] </p></td>
                        <td>{result[7]}</td>
                        <td>--</td>
                        </tr>
                        <tr>
                        <td><p style="color:red">Transmissibility [TR] </p></td>
                        <td>{result[8]}</td>
                        <td>--</td>
                        </tr>
                        </table>
                        {result[9]}
                        <b>                 Transmissiblity vs Frequency Ratio Graph(log-log)</b>
                        </br>
                        <p><a href="/">Click here to calculate again</a>
                        </br>
                        <br/>
                                     <br/>
                                                   <p><h2>Definitions:</h2><br/>
                                                   <b>Critical damping:</b> The minimum amount of viscous damping that results in a displaced system returning to its original position without oscillation. <br/>
                                                    </br>
                                                    <b>Damped natural frequency:</b> In the presence of damping, the frequency at which the system vibrates when disturbed. Damped natural frequency is less than undamped natural frequency.<br/>
                                                    </br>
                                                    <b>Damping ratio:</b> The ratio of actual damping to critical damping. It is a dimensionless measure describing how oscillations in a system decay after a disturbance.<br/>
                                                    </br>
                                                    <b>Forced vibrations:</b> Oscillations about a system's equilibrium position in the presence of an external excitation.<br/>
                                                    </br>
                                                    <b>Free  vibrations:</b> Oscillations about a system's equilibrium position in the absence of an external excitation.<br/>
                                                    </br>
                                                    <b>Natural frequency:</b> The frequency at which a system vibrates when set in free vibration.<br/>
                                                    </br>
                                                    <b>Undamped natural frequency:</b> In the absence of damping, the frequency at which the system vibrates when disturbed.<br/>
                                                    </br>
                                                    <b>Period of Oscillation:</b> The time in seconds required for one cycle.<br/>
                                                    </br>
                                                    <b>Transmissiblity:</b> The ratio of output amplitude to input amplitude at same frequency. Following 2 conditions have same transmissiblity value.<br/>
                                                    <p>-- Transmissiblity between harmonic motion excitation from the base (input) and motion response of mass (output) Ex: Car runing on the road. Car body is m, base motion excitation is road disturbances.</p>
                                                    <p style="text-align:center"><img src="https://amesweb.info/Vibration/images/SDOF_BaseDriven.jpg" alt="Italian Trulli"></p>
                                                    <p>-- Harmonic forcing excitation to mass (Input) and force transmitted to base (output). Ex: A rotating machine generating force during operation and transmitting to its base.</p>
                                                    <p style="text-align:center"><img src=https://amesweb.info/Vibration/images/SDOF_MassDriven.jpg></p>
                                                    <br>
                                                    <b>Quality Factor:</b> Transmissibility at resonance, which is the system’s highest possible response ratio.<br/>
                                                   </br>
                                                     <br/>
                                                     <h3>Single Degree of Freedom Vibration Equations:</h3>
                                                     <a data-flickr-embed="true" href="https://www.flickr.com/photos/192618941@N08/51054280162/in/dateposted/" title="Capture"><img src="https://live.staticflickr.com/65535/51054280162_92a7700327_b.jpg" width="700" height="500" alt="Capture"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>
                                                     </br>
                                                     </br>

                                     </br>
                                     </br>
                                     <p><a href="/">Click here to calculate again</a>
                                     </br>
                    </body>
                    </html>
            '''.format(result=result)
    return '''
        <html>
            <body>
                {errors}
                    <body style="background-color:powderblue;">
                <h1 style="text-align:center;color:brown;background-color:yellow;"> SINGLE DEGREE OF FREEDOM SYSTEMS (SDOF)</p></h1>
                <h1 style="text-align:center;color:brown;background-color:yellow">- VIBRATION CALCULATOR</p></h1>
                <br/>
                      <p><b>The Single Degree of Freedom (SDOF) Vibration Calculator</b> to calculate mass-spring-damper natural frequency, circular frequency, damping factor, Q factor, critical damping, damped natural frequency and transmissibility for a harmonic input.
                  Mechanical vibrations are fluctuations of a mechanical or a structural system about an equilibrium position. Mechanical vibrations are initiated when an inertia element is displaced from its equilibrium position due to energy input to the system through an external source. When work is done on SDOF system and mass is displaced from its equilibrium position, potential energy is developed in the spring.
                  A restoring force or moment pulls the element back toward equilibrium and this cause conversion of potential energy to kinetic energy. In the absence of nonconservative forces, this conversion of energy is continuous, causing the mass to oscillate about its equilibrium position.
                  All structures have many degrees of freedom, which means they have more than one independent direction in which to vibrate and many masses that can vibrate. Single degree of freedom systems are the simplest systems to study basics of mechanical vibrations. SDOF systems are often used as a very crude approximation for a generally much more complex system. The other use of SDOF system is to describe complex systems motion with collections of several SDOF systems.
                  </br>
                  </br>

                <form method="post" action=".">
                    <label for="operation"><h2>Operation:</h2></label>
                    <select id="operation" name="operation">
                    <option value="+"><b>Free Vibration-></b></option>
                    <option value="-"><b>Forced Vibration-></b></option>
                    </select>
                    <br/>
                    <br/>

                    <br/>
                    <label for="number1">Mass [m] (in kg) :.......................................</label>
                    <input type="text" name="number1" id="number1">

                    <label for="unit1">Unit:</label>
                    <select id="unit1" name="unit1">
                    <option value="11"><h4><b>kg</b></h4></option>
                    <option value="12"><h4><b>gram</b></h4></option>
                    <option value="13"><h4><b>lb</b></h4></option>
                    </select>
                    <br/>

                    <br/>
                    <label for="number2">k (in N/m) :.................................................</label>
                    <input type="text" name="number2" id="number2">

                    <label for="unit2">Unit:</label>
                    <select id="unit2" name="unit2">
                    <option value="21"><h4><b>N/m</b></h4></option>
                    <option value="22"><h4><b>N/mm</b></h4></option>
                    <option value="23"><h4><b>lbf/in</b></h4></option>
                    </select>

                    <br/>
                    <br/>
                    <label for="number3">Damping ratio (coefficient) [ζ] :................</label>
                    <input type="text" name="number3" id="number3">
                    <br/>
                    <br/>
                    <label for="number4">Harmonic input frequency [Ω] (in Hz) :...</label>
                    <input type="text" name="number4" id="number4">
                    <label for="unit3">Unit:</label>
                    <select id="unit3" name="unit3">
                    <option value="11"><h4><b>Hz</b></h4></option>
                    </select>
                    </br>
                    (Enter 0 if it is free vibration)
                    <br/>

                    <br/>
                    <br/>
                    <input type="submit" value="Submit"/>
                    <input type="reset"  value="RESET" style="color: red;"/>
                </form>

            </body>
        </html>
    '''.format(errors=errors)

if __name__ == '__main__':
    app.debug = True
    app.run()
