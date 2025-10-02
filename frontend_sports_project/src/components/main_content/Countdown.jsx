import { useEffect, useState } from "react";

export default function Countdown({ dateEvent, strTime }) {
    const [days, setDays] = useState(0);
    const [hours, setHours] = useState(0);
    const [minutes, setMinutes] = useState(0);
    const [seconds, setSeconds] = useState(0);

    useEffect(() => {
        const targetDate = new Date(`${dateEvent}T${strTime}`);

        function updateCountdown() {
            const now = new Date().getTime();
            const distance = targetDate - now;

            if (distance <= 0) {
                setDays(0);
                setHours(0);
                setMinutes(0);
                setSeconds(0);
                return;
            }

            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            setDays(days);
            setHours(hours);
            setMinutes(minutes);
            setSeconds(seconds);
        }

        updateCountdown();
        const interval = setInterval(updateCountdown, 1000);
        return () => clearInterval(interval);
    }, [dateEvent, strTime]);

    return (
        <div className="countdown">
            <h3>Countdown:</h3>
            <p><strong>{days}d {hours}h {minutes}m {seconds}s</strong></p>
            <p><strong>Date:</strong> {dateEvent}</p>
            <p><strong>Time:</strong> {strTime}</p>
        </div>
    ) 
}
